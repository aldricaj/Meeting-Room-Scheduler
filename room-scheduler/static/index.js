function saveToLocal(keyName, obj) {
	localStorage.setItem(keyName, JSON.stringify(obj))
}

function loadFromLocal(keyName) {
	return JSON.parse(localStorage.getItem(keyName))
}

function addRoom(obj) {
	var rooms = loadFromLocal('rooms');
  
  if (rooms == undefined) {
  	rooms = []
  }
  
  rooms.push(obj)
  
  saveToLocal('rooms', rooms);
}

function getRooms() {
	return loadFromLocal('rooms')
}

function addMeeting(obj) {
	var meetings = loadFromLocal('meetings');
  
  if (meetings == undefined) {
  	meetings = []
  }
  
  meetings.push(obj)
  
  saveToLocal('meetings', meetings);
}

function getMeetings() {
	return loadFromLocal('meetings')
}

function addPerson(obj) {
	var persons = loadFromLocal('persons');
  
  if (persons == undefined) {
  	persons = []
  }
  
  persons.push(obj)
  
  saveToLocal('persons', persons);
}

function getPersons() {
	return loadFromLocal('persons')
}

function addOrg(obj) {
	var orgs = loadFromLocal('orgs');
  
  if (orgs == undefined) {
  	orgs = []
  }
  
  orgs.push(obj)
  
  saveToLocal('orgs', orgs);
}

function getOrgs() {
	return loadFromLocal('orgs')
}

if (!loadFromLocal('ran')) {
  console.log('Adding Data');
  addOrg({
    orgId: 1,
    orgName: "Test Organization 1"
  })
  
  addOrg({
    orgId: 2,
    orgName: "Test Organization 2"
  })
  
  addPerson({
    orgId: 1,
    username: "jabrams",
    firstName:"John",
    lastName: "Smith",
    email:"jsmith@nowhere.com",
    role: { roleId: 1, roleName: "Administrator"}
  });
  
  addPerson({
    orgId: 1,
    username: "jdoe",
    firstName:"John",
    lastName: "Doe",
    email:"jdoe@nowhere.com",
    role: { roleId: 2, roleName: "user"}
  });
  
  addPerson({
    orgId: 1,
    username: "jdoe2",
    firstName:"Jane",
    lastName: "Doe",
    email:"jdoe2@nowhere.com",
    role: { roleId: 2, roleName: "user"}
  });
  
  addPerson({
    org_id: 1,
    username: "alovelace",
    first_name:"Ada",
    last_name: "Lovelace",
    email:"alovelace@nowhere.com",
    role: { role_id: 2, role_name: "user"}
  });
  
  addRoom({
    orgId: 1,
    roomNumber: "1",
    avType: {
      avTypeId: 1,
      avTypeText:"None"
    },
    schedule: [
      {
        meeting_id: 1,
        meeting_start: new Date(2018, 6, 25, 9, 0),
        meeting_end: new Date(2018, 6, 25, 10, 0),
        meeting_title: "Post Mortem"
      },
      {
        meeting_id: 2,
        meeting_start: new Date(2018, 6, 26, 13,0),
        meeting_end: new Date(2018, 6, 26, 14,0),
        meeting_title: "Sprint Planning"
      }
    ]
  });
  
  addRoom({
    orgId: 1,
    roomNumber: "2",
    avType: {
      avTypeId: 2,
      avTypeText:"Projector"
    },
    schedule: [
      {
        meeting_id: 3,
        meeting_start: new Date(2018, 6, 24, 14, 0),
        meeting_end: new Date(2018, 6, 24, 16, 0),
        meeting_title: "Long Meeting"
      },
      {
        meeting_id: 4,
        meeting_start: new Date(2018, 6, 26, 13,0),
        meeting_end: new Date(2018, 6, 26, 14,0),
        meeting_title: "Short Meetings"
      }
    ]
  });
  
  addRoom({
    orgId: 1,
    roomNumber: "3",
    avType: {
      avTypeId: 3,
      avTypeText:"Television"
    },
    schedule: [
      {
        meeting_id: 6,
        meeting_start: new Date(2018, 6, 24, 12, 0),
        meeting_end: new Date(2018, 6, 24, 16, 0),
        meeting_title: "Ultra Long Meeting"
      },
      {
        meeting_id: 7,
        meeting_start: new Date(2018, 6, 27, 13,0),
        meeting_end: new Date(2018, 6, 27, 14,0),
        meeting_title: "Short Meetings"
      }
    ]
  });
  saveToLocal('ran', "true")
  }
$(document).ready(function(){
  
  var meetingRooms = getRooms();
  meetingRooms.forEach(function(meetingRoom){
    $(".allRooms").append("<div class='box effect8'><div class='col-sm-12 room'><div class='room-number col-sm-6'><h2>Room "+meetingRoom.roomNumber+"</h2></div><div class='col-sm-6'><a id='newMeeting' style='float: right; margin-top: 24px;'><h4>+ Add New Meeting </h4></a></div></div><hr><div class='col-sm-6'>{{Meeting.meetingName}}</div><div class='col-sm-6'>{{Meeting.startTime}} - {{Meeting.endTime}}</div> <div class='col-sm-10'><table align='center' style='width:100%'><tr><th></th><th>8am</th> <th>9am</th><th>10am</th><th>11am</th><th>12pm</th><th>1pm</th><th>2pm</th><th>3pm</th><th>4pm</th><th>5pm</th><th>6pm</th><th>7pm</th></tr><tr><th>Mon</th><td></td> <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><th>Tues</th><td></td> <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><th>Wed</th><td></td> <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><th>Thurs</th><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><th>Fri</th><td></td> <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><th>Sat</th><td></td> <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><th>Sun</th><td></td> <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table></div><div class='col-sm-2' style='position: absolute;bottom: 0;right: -50px;'><p>Media Availability:</p> <div class='circle green'></div><br /><p>AV Type: Projector</p></div></div><script>var modal = document.getElementById('myModal');	var btn = document.getElementById('newMeeting');var span = document.getElementsByClassName('close')[0];var submit = document.getElementsByClassName('btn')[0];btn.onclick = function() {modal.style.display = 'block';}span.onclick = function() {modal.style.display = 'none';}submit.onclick = function() {modal.style.display = 'none'}window.onclick = function(event) {if (event.target == modal) {modal.style.display = 'none';}}</script>")
  });
  if(window.location.href === "http://localhost:5080/"){
    $("[href='/']").hide()
    $("[href='/dashboard']").hide()
    $("[href='/admin-page']").hide()

  }
  else {
    $("[href='/']").show()
    $("[href='/dashboard']").show()
    $("[href='/admin-page']").show()
  }
});