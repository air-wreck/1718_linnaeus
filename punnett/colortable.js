/* note: styling for the table (besides data coloring) should be set by the
         caller, not the callee */

function colortbl(data, colors) {
  /* return an html string with a table based on given data

  Parameters:
    String[][] data : the data
    String[][][] colors : the colors --- please match the data array
  */

  var html_str = '<table>';
  for (var r = 0; r < data.length; r++) {
    html_str += '<tr>';
    for (var c = 0; c < data.length; c++) {
      if (r == 0 || c == 0) {
        html_str += '<th>'+data[r][c].toString()+'</th>';
      } else {
        /* for data cells, pick background based on parallel color array */
        style = '';  // style defaults to nothing
        if (colors[r][c].length == 1) {
          style = 'background-color: '+colors[r][c].toString()+';';
        } else if (colors[r][c].length == 2) {
          style = 'background: linear-gradient(-45deg,'
                  +colors[r][c][0].toString()+' 50%,'
                  +colors[r][c][1].toString()+' 51%);'
        }
        html_str += '<td style="'+style+'">'+data[r][c].toString()+'</td>';
      }
    }
    html_str += '</tr>'
  }
  return html_str;
}
