/* ped_solve.js

implements ped_solve.py, except in Javascript */

// the module structure allows us to keep infection functions private
const ped_solve = (function () {

  /* infect_* functions determine the probability that an individual is
     infected based on the necessary information */

     
 //REPLACE INDIV WITH ARRAY INDEXES
  function bottomUp(marriage) {
    var infected = false;
    // if kid infected parents are carriers unless infected already
    marriage[2].forEach(indiv => {
      if (indiv.infected === true && indiv.father.infected === false) {
        indiv.father.carrier = 1;
        indiv.father.infected = false;
        indiv.father.final = true;
      }
      if (indiv.infected === true && indiv.mother.infected === false) {
        indiv.mother.carrier = 1;
        infected = false;
        indiv.mother.final = true;
      }
    })
    if (infected === false) {
      // if child is carrier but parents are unknown and aren't infected then, parents have 2/3 chance
      marriage[2].forEach(indiv => {
        if (indiv.carrier === 1 && indiv.mother.carrier != 1 && indiv.mother.infected != true && indiv.father.infected != true && indiv.mother.final === false && indiv.father.final === false) {
          test.mother.carrier = 2/3;
          test.father.carrier = 2/3;
        }
    });
    //if kid is unknown... go to parents top-down
  }
 
  function topDown(marriage) {
     //if mom and dad are both carriers but not infected then child is has 2/3 chance of being carrier if not infected
    if (marriage[0].carrier === 1 && marriage[1].carrier === 1 && marriage[1].infected === false && marriage[0].infected === false){
      marriage[2].forEach(indiv => {
        if (indiv.infected != 1){
          indiv.carrier = 2/3;
        }
      }
    })
      //mom and dad are purely dominant
    if (marriage[0].carrier === 0 && marriage[0].infected === false && marriage[1].carrier === 0 && marriage[1].infected === false) {
      marriage[2].forEach(indiv => {
        indiv.infected = false;
        indiv.carrier = 0;
      })
    }
    //one of the parents is a carrier the other is AA, thus child has 50% chance of being Aa
    if ((marriage[0].carrier === 1 && marriage[1].carrier === 0 && marriage[1].infected === false) || (marriage[0].carrier === 1 && marriage[1].carrier === 0 && marriage[1].infected === false)) {
      marriage[2].forEach(indiv => {
        indiv.infected = false;
        indiv.carrier = 0.5;
      })
    }
    //one parent is aa, one is Aa, thus child is carrier if not infected
    if ((marriage[0].infected === true && marriage[1].carrier === 1 && marriage[1].infected === false) || (marriage[1].infected === true && marriage[0].carrier === 1 && marriage[0].infected === false)) {
      marriage[2].forEach(indiv => {
        if (indiv.infected === 0){
          indiv.infected = false;
          indiv.carrier = 1;
        }
      })
    }
    //one parent infected, other is pure, then the kid's a carrier
    if ((marriage[0].infected === true && marriage[1].carrier === 0 && marriage[1].infected === false) || (marriage[1].infected === true && marriage[0].carrier === 0 && marriage[0].infected === false)) {
      marriage[2].forEach(indiv => {
        indiv.carrier = 1;
      })
    }
  }

  function solved (marriages) {
    marriages.forEach(marriage => {
      if (marriage[0].final === true && marriage[1].final === true){
        marriage[2].forEach(indiv => {
          if(marriage[2].final == false) {
            return;
          }
        })
        marriages.remove(marriage);
        if (marriages[0] === null){
          return true;
        }
      }
    })
  }
  /*
  function parentToChild(marriage) {
    marriage[2].forEach(indiv => {
      if (indiv.carrier === 1 && indiv.mother.carrier != 1) {
        test.mother.carrier = 2/3;
      }
      if (indiv.carrier === 1 && indiv.father.carrier != 1) {
        test.father.carrier = 2/3;
      }
  }
  */
  return {
    /* enumerated type for sex */
    Sex: {m: "male", f: "female"},

    /* the Person object represents an individual
       it forms the node in our linked directed acyclic graph */
    Person: function (name, sex, infected=false) {
      this.father = null;  // link to parent Person objects
      this.mother = null;
      this.name = name;    // object is identified by unique String
      this.sex = sex;      // see Sex enum type
      this.infected = infected;  // has disease?
      this.carrier = -1;
      this.final = false;

      // set parent Person nodes
      this.add_parents = (father, mother) => {
        this.father = father;
        this.mother = mother;
      }

      // conveniently return info as an array
      this.get = () =>
        [this.name, this.sex, this.infected];
    },

    /* recursively determine probability for a given person
       ooh, what if we made this anonymous and recursed with a Y-combinator? */
    find_prob: function find_prob(person, method) {
      // choose the infection function based on the passed parameter "method"
      // method is guaranteed to be valid, at least in the select form
      method = method || "avg";
      methods = {
        "avg": infect_avg,
        "auto_dom": infect_auto_dom
      }
      const infect_func = methods[method];

      if (person.infected >= 0)
        // this person has an independent probability
        return person.infected;

      // for now, we assume that the pedigree is correct: each person without
      // an independent probability has two linked parent nodes in the pedigree
      // we recursively travel up the pedigree to get child probability
      f = find_prob(person.father, method);
      m = find_prob(person.mother, method);
      person.infected = infect_func(f, m);
      return person.infected;
    },

    /* description:
       solve pedigree combinatorically by building candidate solutions top-down
       essentially, we go through the top generation, see what genotypes are
       possible, then go down to the next generation and determine possible
       genotypes based on the previous generation and this generation's known
       characteristics. then, we go back up the tree, removing candidates that
       are now invalid. when we have done this for each generation, we have a
       tree with all possible genotype combinations. then we solve individual
       punnett squares to determine the probability of each genotype

       interface:
         parameters:
           pedigree :: [Person], a list of linked nodes of Person objects
                                 no error checking is performed here
         returns:
           solution :: [Person], this function mutates the state of the passed
                                 pedigree list, but it also returns it for more
                                 convenient chaining
       */

    /* actually, new description of algorithm:
      0. if no infected individuals, reject the tree as invalid
      1. label all infected individuals as carrier: +1
      2. if there are no more negative carrier values, the tree is solved
      3. otherwise, each infected individual spreads their probability to one
         generation up and down
         if two contradictory things clash, we reject the tree as invalid

      e.g.
      [ ] --- ( )
           |
          (+)
    */
    solve_auto_rec: pedigree => {
      if (!pedigree.some(person => person.infected)) return -1; // no infected!

      pedigree.forEach(person => {
        if (person.infected) person.carrier = +1;
      });

      while (pedigree.some(person => person.carrier < 0)) {
        // do something
      }
      return 1; // all individuals have defined carrier values, return success
    }
  };
}());
