/* pun_solve.js

functions for solving punnett squares */

const pun_solve = (function () {
  /* transforms a genotype string description into a 2D array, e.g.
     "AaBbCc" -> [["A", "a"], ["B", "b"], ["C", "c"]] */
  const str2geno = string =>
    string.split("")
          .map((el, i) => [el, string[i+1]])
          .filter((_, i) => i % 2 === 0);

  /* recursively determines the possible offspring for 2D genotype array */
  const combine = (arr, depth) => {
    if (depth === arr.length) return [""];

    var res = [];
    for (let i in arr[depth]) {
      let tmp = combine(arr, depth+1);
      for (let j in tmp)
        res.push(arr[depth][i]+tmp[j]);
    }
    return res;
  }

  /* weaves two gentotype strings together, e.g.
     add("ABC", "abc") -> "AaBbCc" */
  const add = (f, m) =>
    f.split("").map((el, i) => [el, m[i]].sort().join("")).join("");

  return {
    /* general solving function for two genotype strings */
    solve: (f, m) => {
      var f_arr = combine(str2geno(f), 0);
      var m_arr = combine(str2geno(m), 0);
      var sol_arr = [];
      for (let i in f_arr) {
        sol_arr.push([]);
        for (let j in m_arr) {
          sol_arr[i].push(add(f_arr[i], m_arr[j]));
        }
      }
      square = [[""].concat(m_arr)];
      for (let i in m_arr) {
        square.push([f_arr[i]].concat(sol_arr[i]));
      }
      return square;
    }
  }
}());
