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
        infected = true;
      }
      if (indiv.infected === true && indiv.mother.infected === false) {
        indiv.mother.carrier = 1;
        infected = true;
      }
    })
    if (infected === false) {
      // if child is carrier but parents are unknown and aren't infected
      marriage[2].forEach(indiv => {
        if (indiv.carrier === 1 && indiv.mother.carrier != 1 && indiv.mother.infected != true) {
          test.mother.carrier = 2/3
        }
        if (indiv.carrier === 1 && indiv.father.carrier != 1 && indiv.father.infected != true) {
          test.father.carrier = 2/3
        }   
    }
    //if kid is unknown... go to parents top-down
  }

  function topDown(marriage) {
    if (marriage[0].carrier === 1 && marriage[1] === 1){
      //do the 2/3 thingies
    }
    if 
  } 

  function parentToChild(marriage) {
    marriage[2].forEach(indiv => {
      if (indiv.mother.carrier === 1 && indiv.mother.carrier != 1) {
        test.mother.carrier = 2/3
      }
      if (indiv.carrier === 1 && indiv.father.carrier != 1) {
        test.father.carrier = 2/3
      }   
  }
  return {
    /* enumerated type for sex */
    Sex: {m: "male", f: "female"},

    /* the Person object represents an individual
       it forms the node in our linked directed acyclic graph */
    Person: function (name, sex, infected=-1.0) {
      this.father = null;  // link to parent Person objects
      this.mother = null;
      this.name = name;    // object is identified by unique String
      this.sex = sex;      // see Sex enum type
      this.infected = infected;  // disease probability
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
    }
  };
}());
