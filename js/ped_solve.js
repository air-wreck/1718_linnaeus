/* =============
File: ped_solve.js
Authors: Eric, Nelson, and Karena
Course: CSE
Description: module exporting functions for solving pedigrees
============= */

const ped_solve = (function () {
  // solving function for pedigree
  return {
    /* enumerated type for sex */
    Sex: {m: "male", f: "female"},

    /* the Person object represents an individual
       it forms the node in our linked directed acyclic graph */
    Person: function (name, sex, infected) {
      this.father = null;  // link to parent Person objects
      this.mother = null;
      this.name = name;    // object is identified by unique String
      this.sex = sex;      // see Sex enum type
      this.infected = infected;  // has disease?
      this.carrier = -1;

      // set parent Person nodes
      this.add_parents = (father, mother) => {
        this.father = father;
        this.mother = mother;
      }

      // conveniently return info as an array
      this.get = () =>
        [this.name, this.sex, this.infected];
    },

    //REPLACE INDIV WITH ARRAY INDEXES
    bottomUp: function bottomUp(marriage) {
      // for each marriage, determine parent probabilities based on kids
       var infected = false;
       var maxcarrier = 0;

       // set parent carrier probabilities as 0 if infected
       if (marriage[0].infected === true) {
          marriage[0].carrier = 0;
        }

       if (marriage[1].infected === true) {
          marriage[1].carrier = 0;
        }

       // check if any kids are infected or carriers
       marriage[2].forEach(indiv => {
         if (indiv.infected === true){
           indiv.carrier = 0;
           infected = true;
         }
         else if (indiv.carrier > maxcarrier){
           maxcarrier = indiv.carrier;
         }
       })

       // if kids are infected, set uninfected parents as carriers
       if (infected === true){
        if (marriage[0].infected === false) {
          marriage[0].carrier = 1;
        }
        if (marriage[1].infected === false){
          marriage[1].carrier = 1;
        }
       } 
       // or if kids are carriers, calculate carrier probability of uninfected parents
       //   as 2/3 * max kid probability
       //   2/3 because of 3 possible uninfected genotypes (AA, Aa, aA), two are carriers
       else if (maxcarrier > 0){
        if (marriage[0].infected === false && marriage[1].infected === false){
          marriage[0].carrier = 2/3 * maxcarrier;
          marriage[1].carrier = 2/3 * maxcarrier;
        }
       }

       //if kid is unknown... go to parents top-down
     },

     topDown: function topDown(marriage) {
        // calculate kid carrier probabilities based on parents 
        
        //if mom and dad are both carriers, then uninfected child has
        //  2/3 chance of being carrier 
        //  thus, multiply 2/3 by average parent carrier probability
       if (marriage[0].carrier > 0 && marriage[1].carrier > 0){
         marriage[2].forEach(indiv => {
           if (indiv.infected === false){
             indiv.carrier = 2/3 * ((marriage[0].carrier
               + marriage[1].carrier)/2);
           } else {
            indiv.carrier = 0;
           }
         });
       }

      //if mom and dad are purely dominant, child carrier probability is 0
       if (marriage[0].carrier === 0 && marriage[0].infected === false
         && marriage[1].carrier === 0 && marriage[1].infected === false) {
         marriage[2].forEach(indiv => {
           indiv.carrier = 0;
         })
       }

       //one of the parents is a carrier and the other is AA, thus child has 50%
       //  chance of being carrier (Aa)
       if ((marriage[0].carrier > 0 && marriage[1].carrier === 0
         && marriage[1].infected === false) || (marriage[1].carrier > 0
         && marriage[0].carrier === 0 && marriage[0].infected === false)) {
         marriage[2].forEach(indiv => {
           indiv.carrier = ((marriage[0].carrier + marriage[1].carrier)/2);
         })
       }

       //one parent is aa, one is Aa, thus child is carrier if not infected
       if ((marriage[0].infected === true && marriage[1].carrier > 0)
       || (marriage[1].infected === true && marriage[0].carrier > 0)) {
         marriage[2].forEach(indiv => {
           if (indiv.infected === false){
             indiv.carrier = 1;
           } else {
            indiv.carrier = 0;
           }
         })
       }

       //one parent infected, other is pure, then the kid's a carrier
       if ((marriage[0].infected === true && marriage[1].carrier <= 0
         && marriage[1].infected === false) || (marriage[1].infected === true
         && marriage[0].carrier <= 0 && marriage[0].infected === false)) {
         marriage[2].forEach(indiv => {
           indiv.carrier = 1;
         })
       }
     },

     solved: function solved (marriages, iterator) {
      //check if all pedigree individuals have been solved
      //    if max number of runs has not been reached, return
      //    false to rerun solving functions
      //    if max number of runs has been reached, set remaining
      //    unknown individuals as having 0 carrier probability
       var solved = true;
         marriages.forEach(marriage => {
          //check first parent 
          if (marriage[0].carrier === -1){
            if (iterator < marriages.length + 1){
              solved = false;
            } else {
              if (marriage[0].father === null){
                marriage[0].carrier = 0;
              }
            }
          }
          //check second parent
          if (marriage[1].carrier === -1){
            if (iterator < marriages.length + 1){
              solved = false;
            } else {
              if (marriage[1].father === null){
                marriage[1].carrier = 0;
              }
            }
          }
          //check children
          marriage[2].forEach(indiv => {
            if(indiv.carrier === -1) {
              if (iterator < marriages.length + 1){
              solved = false;
            }
            }
          });
        });

       return solved;
     },
  };
}());
