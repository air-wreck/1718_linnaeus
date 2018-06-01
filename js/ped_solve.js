/* ped_solve.js

implements ped_solve.py, except in Javascript */

// the module structure allows us to keep infection functions private
const ped_solve = (function () {

  /* infect_* functions determine the probability that an individual is
     infected based on the necessary information */

  // use average of parent probabilities, just for testing
  const infect_avg = (f, m) => 0.5 * (f + m);

  // autosomal dominant: only parent probabilities matter, since no carriers
  const infect_auto_dom = (f, m) => {
    // consider the probability that a child is NOT infected: both parents must
    //   pass on recessive (a) alleles
    // if a parent is not infected (aa), there is a 2/2 chance of this
    // if a parent is infected (AA, Aa, aA), there is a 2/6 chance of this
    // then the probability of each parent passing on a harmless (a) is:
    //   1/3 * (prob. parent infected) + (prob. parent clean)
    // where
    //   (prob. parent clean) = 1 - (prob. parent infected)
    // we multiply the father and mother probabilities to get prob. child clean
    let f_pass_clean = f/3 + (1 - f);
    let m_pass_clean = m/3 + (1 - m);
    return 1 - (f_pass_clean * m_pass_clean);
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
