/* ped_solve.js

implements ped_solve.py, except in Javascript */

/* enumerated type for sex */
const Sex = {m: "male", f: "female"};

/* the Person object represents an individual
   it forms the node in our linked directed acyclic graph */
function Person(name, sex, infected=-1.0) {
  this.father = null;  // link to parent Person objects
  this.mother = null;
  this.name = name;    // object is identified by unique String
  this.sex = sex;      // see Sex enum type
  this.infected = infected;  // disease probability

  // set parent Person nodes
  this.add_parents = (father, mother) => {
    this.father = father;
    this.mother = mother;
  }

  // conveniently return info as an array
  this.get = () =>
    [this.name, this.sex, this.infected];
}

/* probability of infection, proof of concept (avg) for now */
const infect = (f, m) => 0.5 * (f + m);

/* recursively determine probability for a given person */
const find_prob = person => {
  if (person.infected >= 0)
    // this person has an independent probability
    return person.infected;

  // for now, we assume that the pedigree is correct: each person without
  // an independent probability has two linked parent nodes in the pedigree
  // we recursively travel up the pedigree to get child probability
  f = find_prob(person.father);
  m = find_prob(person.mother);
  person.infected = infect(f, m);
  return person.infected;
}
