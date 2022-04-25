setUplogin();
showCanvas();
var text = "";
var passwords= ["AOL: password",  "Amazon: Pizza",  "Pizza Hut: River123", "Gmail: Treat78", "Code.org: Eaton74", "Sky Sports: Mini14", "Electron: password1"];
onEvent("passwordsbutton", "click", function() {
  showPasswords();
});
showCanvas();
onEvent("gobackbutton", "click", function() {
  setScreen("welcomescreen");
});
showCanvas();
onEvent("photosbutton", "click", function() {
  setScreen("photoscreen");
});
onEvent("gobackbutton2", "click", function() {
  setScreen("welcomescreen");
});
onEvent("contactsbutton", "click", function() {
  setScreen("contactscreen");
});
showCanvas();
onEvent("addnewcontactbtn", "click", function() {
  setScreen("addnewcontactscreen");
});
showCanvas();
onEvent("xbutton", "click", function() {
  setScreen("contactscreen");
});
onEvent("gobackbutton3", "click", function() {
  setScreen("welcomescreen");
});
onEvent("checkbutton", "click", function() {
  displayNewcontact();
});
onEvent("button6", "click", function() {
  setScreen("yanewcontact");
  makeContact();
});
showCanvas();
onEvent("musicbutton", "click", function() {
  setScreen("musicscreen");
});
showCanvas();
onEvent("playbtn", "click", function() {
  playSound("Ta5bXL20piMZ.128.mp3", false);
  stopSound("» want me «.mp3");
  stopSound("BgUuKyrLxoh5.128.mp3");
});
onEvent("playbtn2", "click", function() {
  playSound("» want me «.mp3", false);
  stopSound("BgUuKyrLxoh5.128.mp3");
  stopSound("Ta5bXL20piMZ.128.mp3");
});
onEvent("playbtn3", "click", function() {
  playSound("BgUuKyrLxoh5.128.mp3", false);
  stopSound("» want me «.mp3");
  stopSound("Ta5bXL20piMZ.128.mp3");
});
onEvent("stopbtn", "click", function() {
  stopSound("Ta5bXL20piMZ.128.mp3");
});
onEvent("stopbtn2", "click", function() {
  stopSound("» want me «.mp3");
});
onEvent("stopbtn3", "click", function() {
  stopSound("BgUuKyrLxoh5.128.mp3");
});
onEvent("gobackbutton4", "click", function() {
  setScreen("welcomescreen");
});
onEvent("gobackbutton5", "click", function() {
  setScreen("contactscreen");
});
onEvent("logoutbtn", "click", function() {
  setScreen("startscreen");
});
onEvent("newpasswordbutton","click",function(){
  setScreen("newpasswordscreen");
});
onEvent("passdone", "click", function( ) {
  setScreen("passwordscreen");
  createPassword();
});
onEvent("xbutton2", "click", function() {
  setScreen("passwordscreen");
});
showCanvas();
function makeContact() {
  var newfirstname = getText("firstnameinput");
  setText("newcontactfirstnamelabel", newfirstname);
  var newlastname = getText("lastnameinput");
  setText("newcontactlastnamelabel", newlastname);
  var newnumber = getText("phonenumberinput");
  setText("newnumberlabel", newnumber);
  var newemail = getText("emailinput");
  setText("newemaillabel", newemail);
  var newcompany = getText("workinput");
  setText("newcompanylabel", newcompany);
  var newaddress = getText("addressinput");
  setText("newaddresslabel", newaddress);
  var newnote = getText("noteinput");
  setText("newnotelabel", newnote);
}
function createPassword() {
  var x = getText("newpassinput");
  insertItem(passwords, passwords.length, x);
  showPasswords();
}
function getInson() {
  showCanvas();
  setUplogin();
  var password = getText("text_input1");
  var username = getText("userinput");
  if (username === "username") {
    if (password === "password1") {
      setScreen("welcomescreen");
    } else  {
      setText("text_input1", "Try again.");
    }
  } else {
    setText("userinput", "Try again.");
  }
}
function displayNewcontact() {
  var name = getText("firstnameinput") + " " + getText("lastnameinput");
  setText("button6", name);
  showElement("button6");
  setScreen("contactscreen");
}
function showPasswords() {
  setScreen("passwordscreen");
  for (var i = 0; i < passwords.length; i++) {
    text += passwords[i] + "\n";
  }
  setText("passwordstextarea", text);
  text="";
}
function showCanvas() {
  setActiveCanvas("startcanvas");
  circle(160, 240, 360);
  setActiveCanvas("welcomecanvas");
  circle(160, 240, 300);
  setActiveCanvas("passwordcanvas");
  circle(160, 240, 300);
  setActiveCanvas("photoscanvas");
  circle(160, 240, 300);
  setActiveCanvas("docscanvas");
  circle(160, 240, 300);
  setActiveCanvas("addnewcontactcanvas");
  circle(160, 240, 300);
  setActiveCanvas("yanewcontactcanvas");
  circle(160, 240, 300);
  setActiveCanvas("musicanvas");
  circle(160, 240, 300);
  setActiveCanvas("newpasswordcanvas");
  circle(160, 240, 300);
}
function setUplogin() {
  showCanvas();
  setScreen("startscreen");
  onEvent("enterbutton", "click", function() {
    getInson();
  });
}