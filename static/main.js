// Code for downloading table as a csv file
// https://stackoverflow.com/questions/15547198/export-html-table-to-csv-using-vanilla-javascript

// Quick and simple export target #table_id into a csv
function download_table_as_csv(table_id, separator = ",") {
  // Select rows from table_id
  var rows = document.querySelectorAll("table#" + table_id + " tr");
  // Construct csv
  var csv = [];
  for (var i = 0; i < rows.length; i++) {
    var row = [],
      cols = rows[i].querySelectorAll("td, th");
    for (var j = 0; j < cols.length; j++) {
      // Clean innertext to remove multiple spaces and jumpline (break csv)
      var data = cols[j].innerText
        .replace(/(\r\n|\n|\r)/gm, "")
        .replace(/(\s\s)/gm, " ");
      // Escape double-quote with double-double-quote (see https://stackoverflow.com/questions/17808511/properly-escape-a-double-quote-in-csv)
      data = data.replace(/"/g, '""');
      // Push escaped string
      row.push('"' + data + '"');
    }
    csv.push(row.join(separator));
  }
  var csv_string = csv.join("\n");
  // Download it
  var filename =
    "export_" + table_id + "_" + new Date().toLocaleDateString() + ".csv";
  var link = document.createElement("a");
  link.style.display = "none";
  link.setAttribute("target", "_blank");
  link.setAttribute(
    "href",
    "data:text/csv;charset=utf-8," + encodeURIComponent(csv_string)
  );
  link.setAttribute("download", filename);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}
// program to get a random item from an array

function getRandomItem(arr) {
  // get random index value
  const randomIndex = Math.floor(Math.random() * arr.length);

  // get random item
  const item = arr[randomIndex];

  return item;
}

teacher_arr = [
  "Mr. Chintu",
  "Mr. Shiva",
  "Mr. Ram",
  "Mr. Shyam",
  "Ms.Bharti",
  "Ms. Bhatt",
  "Mr. Kumar",
];

function autoFill() {
  document.getElementById("teacher_1_name").value = "a";
  document.getElementById("teacher_1_subj").value = "English";
  document.getElementById("teacher_1_grades").value = "1,2,3,4,5";

  document.getElementById("teacher_2_name").value = "b";
  document.getElementById("teacher_2_subj").value = "Maths";
  document.getElementById("teacher_2_grades").value = "1,2,3,4,5";

  document.getElementById("teacher_3_name").value = "c";
  document.getElementById("teacher_3_subj").value = "Science";
  document.getElementById("teacher_3_grades").value = "1,2,3";

  document.getElementById("teacher_4_name").value = "d";
  document.getElementById("teacher_4_subj").value = "Social";
  document.getElementById("teacher_4_grades").value = "1,2,3";

  document.getElementById("teacher_5_name").value = "e";
  document.getElementById("teacher_5_subj").value = "Japanese";
  document.getElementById("teacher_5_grades").value = "1,2,3";

  document.getElementById("teacher_6_name").value = "f";
  document.getElementById("teacher_6_subj").value = "Science";
  document.getElementById("teacher_6_grades").value = "4,5";

  document.getElementById("teacher_7_name").value = "g";
  document.getElementById("teacher_7_subj").value = "Social";
  document.getElementById("teacher_7_grades").value = "4,5";

  document.getElementById("teacher_8_name").value = "h";
  document.getElementById("teacher_8_subj").value = "Maths";
  document.getElementById("teacher_8_grades").value = "4,5";

  document.getElementById("teacher_9_name").value = "i";
  document.getElementById("teacher_9_subj").value = "English";
  document.getElementById("teacher_9_grades").value = "6,7,8";

  document.getElementById("teacher_10_name").value = "j";
  document.getElementById("teacher_10_subj").value = "Science";
  document.getElementById("teacher_10_grades").value = "6,7,8";

  document.getElementById("teacher_11_name").value = "k";
  document.getElementById("teacher_11_subj").value = "Social";
  document.getElementById("teacher_11_grades").value = "6,7,8,9";

  document.getElementById("teacher_12_name").value = "l";
  document.getElementById("teacher_12_subj").value = "Maths";
  document.getElementById("teacher_12_grades").value = "6,7,8,9";

  document.getElementById("teacher_13_name").value = "m";
  document.getElementById("teacher_13_subj").value = "Social";
  document.getElementById("teacher_13_grades").value = "6,7,8,9";

  document.getElementById("teacher_14_name").value = "n";
  document.getElementById("teacher_14_subj").value = "English";
  document.getElementById("teacher_14_grades").value = "9,10,11,12";

  document.getElementById("teacher_15_name").value = "o";
  document.getElementById("teacher_15_subj").value = "Phsyics";
  document.getElementById("teacher_15_grades").value = "10,11,12";

  document.getElementById("teacher_16_name").value = "p";
  document.getElementById("teacher_16_subj").value = "Chemistry";
  document.getElementById("teacher_16_grades").value = "10,11,12";

  document.getElementById("teacher_17_name").value = "q";
  document.getElementById("teacher_17_subj").value = "Computers/Bio";
  document.getElementById("teacher_17_grades").value = "10,11,12";

  document.getElementById("teacher_18_name").value = "5";
  document.getElementById("teacher_18_subj").value = "English";
  document.getElementById("teacher_18_grades").value = "10,11,12";
}
