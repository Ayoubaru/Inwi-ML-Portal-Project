// SIDEBAR TOGGLE

var sidebarOpen = false;
var sidebar = document.getElementById("sidebar");

function openSidebar() {
  if(!sidebarOpen) {
    sidebar.classList.add("sidebar-responsive");
    sidebarOpen = true;
  }
}

function closeSidebar() {
  if(sidebarOpen) {
    sidebar.classList.remove("sidebar-responsive");
    sidebarOpen = false;
  }
}



$(document).ready(function() {
  var rowsToShow = 5;
  var totalRows = parseInt("{{ total_rows }}");
  var currentRows = rowsToShow;

  function showRows() {
    $('.data-table tr').hide();
    $('.data-table tr').slice(0, currentRows).show();
  }

  function updateButtonState() {
    if (currentRows >= totalRows) {
      $('#view-more-btn').hide();
      $('#collapse-btn').hide();
    } else {
      $('#view-more-btn').show();
      $('#collapse-btn').hide();
    }
  }

  $('#view-more-btn').click(function() {
    currentRows += rowsToShow;
    showRows();
    updateButtonState();
  });

  $('#collapse-btn').click(function() {
    currentRows = rowsToShow;
    showRows();
    updateButtonState();
  });

  showRows();
  updateButtonState();
});
