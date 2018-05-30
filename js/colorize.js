/* colorize.js

functions for different color mappings for use in punnett.html
each function represents a different colorization scheme, e.g. codominant

for each function, the following API is specified:
  parameters:
    cell :: String, a genotype description like "AaBBcC"
    colorspace :: Object, a colorspace object returned by sample_colors(n)
                          this is used since it's less efficient to generate
                          the colorspace each time we map to a cell
  returns:
    colors :: [String], a list of hex colors to use for that cell,
                        like ["#ffffff", "#000000"] for 50% white/50% black

  it is permissible to omit parameters for calls to colorize.color_blank and
  colorize.color_random only */

const colorize = (function () {
  let is_dom = g => g === g.toUpperCase();

  return {
    // no colorization
    color_blank: (cell, colorspace) => [],

    // dummy colorization: just to test if the cells shade properly
    color_random: (cell, colorspace) => {
      // randomly choose between 0, 1, 2, or 4 colors
      let tmp = Math.random();
      if (tmp < 0.25) return [];
      if (tmp < 0.50) return ["#f26e46"];
      if (tmp < 0.75) return ["#f26e46", "#4286f4"];
      return ["#f26e46", "#ffbca8", "#4286f4", "#a8c9ff"];
    },

    // each unique trait (A/a) is assigned a single color (light or dark
    // depending on dominant or recessive), and the cell is shaded the color of
    // all its alleles
    color_codominance: (cell, colorspace) => {
      colors = [];
      for (let i = 0; i < cell.length; i += 2) {
        let c_i = Math.round(i / 2);
        if (is_dom(cell[i])) colors.push(colorspace.main[c_i]);
        else colors.push("#fff");

        // append second color only if different
        if (is_dom(cell[i+1]) && !colors.includes(colorspace.main[c_i]))
          colors.push(colorspace.main[c_i]);
        else if (!is_dom(cell[i+1]) && !colors.includes("#fff"))
          colors.push("#fff");
      }
      return colors.reverse();
    },

    // each pair (Aa) if assigned a color, and is represented by either a dark
    // or light color based on whether the it is dominant (AA, Aa, aA) or
    // recessive (aa): essentially a simple dominant/recessive coloring
    color_autosomal: (cell, colorspace) => {
      let colors = [];
      for (let i = 0; i < cell.length; i += 2) {
        let c_i = Math.round(i / 2);
        if (is_dom(cell[i]) || is_dom(cell[i+1]))
          colors.push(colorspace.main[c_i]);
        else
          colors.push("#fff");
      }
      return colors.reverse();
    },

    color_incomplete: (cell, colorspace) => {
      let colors = [];
      for (let i = 0; i < cell.length; i += 2) {
        let c_i = Math.round(i / 2);
        if (is_dom(cell[i]) && is_dom(cell[i+1]))
          colors.push(colorspace.main[c_i]);
        else if (is_dom(cell[i]) || is_dom(cell[i+1]))
          colors.push(colorspace.secondary[c_i]);
        else
          colors.push("#fff");
      }
      return colors.reverse();
    },

    color_xlinked: (cell, colorspace) => {
      pretty.warn_user("x-linked has not yet been implemented");
      return [];
    },

    /* returns an array of colors from a rainbow gradient with
       a given number of sample points (n)

       consider switching to chroma.js for better results (if less fun) */
    sample_colors: n => {
      // we represent main sequence colors as tuples (R,G,B), with each channel
      // restricted to the range 65-244
      // order of transformation:
      //   1. increase G +179: 179
      //   2. decrease R -179: 358
      //   3. increase B +179: 537
      //   4. decrease G -179: 716
      //   5. increase R +179: 895
      //   6. does anyone really care about the pinks?
      // this is a total of 895 delta chroma (i just made that term up)
      // +5 for repetition
      let main = [244, 65, 65];
      let chroma = {main: [], secondary: []};
      let chroma_append = (channel, start=65, stop=244) => {
        let push_colors = C => {
          // increment main channel
          main[channel] = C;
          chroma.main.push(Array.from(main));
          // increase the secondary channels by the appropriate amount
          chroma.secondary.push(main.map(c => Math.round(0.5 * c + 122)));
        }
        if (start <= stop)
          for (let C = start; C <= stop; C++) push_colors(C);
        else
          for (let C = start; C >= stop; C--) push_colors(C);
      }
      chroma_append(1, start=65, stop=244);
      chroma_append(0, start=244, stop=65);
      chroma_append(2, start=65, stop=244);
      chroma_append(1, start=244, stop=65);
      chroma_append(0, start=65, stop=244);

      let rgb_to_hex = rgb =>
        "#"+rgb.map(d => ("0"+d.toString(16)).slice(-2)).join("");

      let samples = {main: [], secondary: []};
      let step = Math.round(chroma.main.length / n);
      for (let i = 0; i < chroma.main.length; i += step) {
        samples.main.push(rgb_to_hex(chroma.main[i]));
        samples.secondary.push(rgb_to_hex(chroma.secondary[i]));
      }
      return samples;
    }
  }
}());
