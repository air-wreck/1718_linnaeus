/* =============
File: ped_draw.js
Authors: Eric, Nelson, and Karena
Course: CSE
Description: module containing functions for plotting a pedigree
  assumes that ped_solve.js has already been included with a <script> tag
============= */

const ped_draw = (function () {
  return {
    Draw: function (title) {
      this.src = "";  // String of Dot source code to render (validate!)
      this.next_hidden = 0;  // next available hidden node ID
      this.nodes = [];  // list of currently existing named nodes

      // create graph and set pedigree attributes
      this.src += `graph {
        graph[splines=ortho];
        node [fixedsize=true fontname=helvetica height=0.5 style=filled];
        labelloc="t";
        label="${title}";`;


      /* BASIC DRAWING FUNCTIONS */

      this.hidden = names => {
        // define hidden nodes from a list
        names.forEach(name =>
          this.src += `"${name}" [shape=point style=invis width=0];`);
      }

      this.indiv = person => {
        // define an individual node from a ped_solve.Person object
        let shape = "square";
        if (person.sex === ped_solve.Sex.f)
          shape = "circle";
        var penetrance = 0;
        if (person.infected === true){
          penetrance = 1;
        }
        // shade the node based on infection probability
        let RGB = [255,
                   Math.round(119 + 136 * (1-penetrance)),
                   Math.round(86 + 169 * (1-penetrance))];
        let color_as_hex = "#"+RGB.map(d =>
          ("0"+d.toString(16)).slice(-2)).join("");

        this.src += `"${person.name}"
          [fillcolor="${color_as_hex}" shape=${shape}];`;
      }

      this.srank = nodes => {
        // places a list of nodes in the same rank
        this.src += `{rank=same; "${nodes.join('" -- "')}";};`;
      }

      this.edges = (edgelist, constraint="true") => {
        // makes a bunch of edges in 2D list
        edgelist.forEach(pair =>
          this.src += `"${pair[0]}" -- "${pair[1]}"
            [constraint=${constraint}];`);
      }

      this.render = () => {
        // return self as DOT language string
        return this.src + "}";
      }


      /* FAMILY PLOTTING FUNCTIONS */

      this.draw_marriage = (father, mother, children) => {
        // accepts two Person objects and draws the marriage between them
        // takes a list of children as arg until i figure out how to do that
        // we'll just assume that the pedigree is valid (error check later?)

        // if unknown, find the probability of disease
        //[father, mother, ...children].forEach(ped_solve.find_prob);

        // append the new people to our list of nodes
        [father, mother]
          .filter(person => !this.nodes.includes(person.name))
          .forEach(person => {
            this.indiv(person);
            this.nodes.push(person.name);
          });
        this.nodes = this.nodes.concat(children.map(child => child.name));

        if (children.length === 0) {
          // no children = no tricky stuff with hidden nodes!
          this.srank([father.name, mother.name]);
        } else {
          // make a hidden node in the middle to connect to children
          this.hidden([this.next_hidden.toString()]);
          this.srank([father.name, this.next_hidden.toString(), mother.name]);
          this.next_hidden++;
        }

        if (children.length === 1) {
          // there is only one child, so no branching for children
          this.indiv(children[0]);
          this.nodes.push(children[0].name);
          this.edges([[(this.next_hidden - 1).toString(), children[0].name]]);
        } else if (children.length > 1){
          // general branching required for children

          // first count number of hidden nodes needed
          let N = Math.round(children.length - (children.length % 2) - 1);
          let hnodes = [...Array(N).keys()]
                        .map(x => x + this.next_hidden)
                        .map(x => x.toString());
          this.hidden(hnodes);
          this.srank(hnodes);

          // link center node to marriage node
          this.edges([[(this.next_hidden - 1).toString(),
                       (this.next_hidden + Math.trunc(N / 2)).toString()]]);
          children.forEach(this.indiv);

          // link the first child to the correct node
          this.edges([[this.next_hidden.toString(), children[0].name]]);

          // link subsequent children to corresponding nodes
          edgelist = children.slice(1, -1).map((child, i) => {
            let add = 0;
            if (children.length % 2 === 0 && i >= Math.trunc(N / 2))
              add = 1;
            return [(this.next_hidden + i + add).toString(), child.name];
          });
          this.edges(edgelist);

          // link the final child to the correct node
          this.edges([[(this.next_hidden + N - 1).toString(),
                       children.slice(-1)[0].name]]);
          this.next_hidden += N;
        }
      }
    }
  }
}());
