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
  "Ms. Bharti",
  "Ms. Bhatt",
  "Mr. Arpan",
  "Ms. Rani",
  "Mr. Kulkarni",
  "Ms. Rishi",
  "Mr. Ayush",
  "Ms. Swati",
  "Mr. Dev",
  "Ms. Priya",
  "Mr. Varun",
  "Ms. Maya",
  "Mr. Surya",
  "Ms. Keerti",
  "Mr. Shreyas",
  "Ms. Gunjan",
  "Mr. Arjun",
  "Ms. Gayathri",
  "Ms. Rekha",
  "Ms. Kaajal",
  "Ms. Radha",
  "Ms. Ananya",
  "Mr. Swayam",
];
function autoFill2() {
  document.getElementById("no_of_periods").value = "10";
  document.getElementById("period_duration").value = "40";
  document.getElementById("no_of_periods").value = "18";
  document.getElementById("start_time").value = "09:00";
  document.getElementById("lunch_period").value = 5;
}
function autoFill() {
  document.getElementById("teacher_1_name").value = "Mr. Chintu";
  document.getElementById("teacher_1_subj").value = "English";
  document.getElementById("teacher_1_grades").value = "1,2,3,4,5";

  document.getElementById("teacher_2_name").value = "Mr. Shiva";
  document.getElementById("teacher_2_subj").value = "Maths";
  document.getElementById("teacher_2_grades").value = "1,2,3,4,5";

  document.getElementById("teacher_3_name").value = "Mr. Kulkarni";
  document.getElementById("teacher_3_subj").value = "Science";
  document.getElementById("teacher_3_grades").value = "1,2,3";

  document.getElementById("teacher_4_name").value = "Ms. Ananya";
  document.getElementById("teacher_4_subj").value = "Social";
  document.getElementById("teacher_4_grades").value = "1,2,3";

  document.getElementById("teacher_5_name").value = "Ms. Rekha";
  document.getElementById("teacher_5_subj").value = "Japanese";
  document.getElementById("teacher_5_grades").value = "1,2,3";

  document.getElementById("teacher_6_name").value = "Ms. Maya";
  document.getElementById("teacher_6_subj").value = "Science";
  document.getElementById("teacher_6_grades").value = "4,5";

  document.getElementById("teacher_7_name").value = "Ms. Rishi";
  document.getElementById("teacher_7_subj").value = "Social";
  document.getElementById("teacher_7_grades").value = "4,5";

  document.getElementById("teacher_8_name").value = "Mr. Ram";
  document.getElementById("teacher_8_subj").value = "Maths";
  document.getElementById("teacher_8_grades").value = "4,5";

  document.getElementById("teacher_9_name").value = "Mr. Shyam";
  document.getElementById("teacher_9_subj").value = "English";
  document.getElementById("teacher_9_grades").value = "6,7,8";

  document.getElementById("teacher_10_name").value = "Ms. Keerti";
  document.getElementById("teacher_10_subj").value = "Science";
  document.getElementById("teacher_10_grades").value = "6,7,8";

  document.getElementById("teacher_11_name").value = "k";
  document.getElementById("teacher_11_subj").value = "Social";
  document.getElementById("teacher_11_grades").value = "6,7,8,9";

  document.getElementById("teacher_12_name").value = "l";
  document.getElementById("teacher_12_subj").value = "Maths";
  document.getElementById("teacher_12_grades").value = "6,7,8,9";

  document.getElementById("teacher_13_name").value = "Mr. Ganshyam";
  document.getElementById("teacher_13_subj").value = "Social";
  document.getElementById("teacher_13_grades").value = "6,7,8,9";

  document.getElementById("teacher_14_name").value = "Ms. Reema";
  document.getElementById("teacher_14_subj").value = "English";
  document.getElementById("teacher_14_grades").value = "9,10,11,12";

  document.getElementById("teacher_15_name").value = "Ms. Radha";
  document.getElementById("teacher_15_subj").value = "Phsyics";
  document.getElementById("teacher_15_grades").value = "10,11,12";

  document.getElementById("teacher_16_name").value = "Mr. Dev";
  document.getElementById("teacher_16_subj").value = "Chemistry";
  document.getElementById("teacher_16_grades").value = "10,11,12";

  document.getElementById("teacher_17_name").value = "Mr. Arpan";
  document.getElementById("teacher_17_subj").value = "Computers/Bio";
  document.getElementById("teacher_17_grades").value = "10,11,12";

  document.getElementById("teacher_18_name").value = "Mr. Ayush";
  document.getElementById("teacher_18_subj").value = "English";
  document.getElementById("teacher_18_grades").value = "10,11,12";
}
