    const lapBtn = document.getElementById('lapBtn');
    const timerMilliSec = document.getElementById('timerMilliSec');
    const timerSec = document.getElementById('timerSec');
    // const timerMins = document.getElementById('timerMins');
    // const timerHrs = document.getElementById('timerHrs');
    const startBtn = document.getElementById('startBtn');
    const resetBtn = document.getElementById('resetBtn');
    const lapRecord = document.getElementById('lapRecord');
    const stepRecord = document.getElementById('stepRecord');
    const xarray = [];
    let x
    
    
    
    
    // let hours = 0;
    // let minutes = 0;
    let seconds = 0;
    let miliseconds = 0;
    
    let displayMilisec = miliseconds;
    let displaySec = seconds;
    // let displayMins = minutes;
    // let displayHours = hours;
    
    let interval = null;
    
    let status = "stopped";
    let lapNow = null;
    let stepNum = null;
    let stepadh = null;
    let y = null;
    
    function start() {
      miliseconds++;
    
      if (miliseconds < 10) displayMilisec = "0" + miliseconds.toString();
      else displayMilisec = miliseconds;
    
      if (seconds < 10) displaySec = "0" + seconds.toString();
      else displaySec = seconds;
    
    //   if (minutes < 10) displayMins = "0" + minutes.toString();
    //   else displayMins = minutes;
    
    //   if (hours < 10) displayHours = "0" + hours.toString();
    //   else displayHours = hours;
    
      if (miliseconds / 100 === 1) {
        seconds++;
        miliseconds = 0;
    
        // if (seconds / 60 === 1) {
        //   minutes++;
        //   seconds = 0;
    
        // //   if (minutes / 60 === 1) {
        // //     hours++;
        // //     minutes = 0;
        //   }
        // }
      }
    
    
      timerMilisec.innerHTML = displayMilisec;
      timerSec.innerHTML = displaySec;
    //   timerMins.innerHTML = displayMins;
    //   timerHrs.innerHTML = displayHours;
    
    }
    
    function startStop() {
      if (status === "stopped") {
        interval = setInterval(start, 10);
        startBtn.innerHTML = "Stop";
        status = "started";
      } else {
        clearInterval(interval);
        startBtn.innerHTML = "Start";
        status = "stopped";
      }
    }
    
    function reset() {
      clearInterval(interval);
      miliseconds = 0;
      seconds = 0;
      stepNum = 0;
    //   minutes = 0;
    //   hours = 0;
      timerMilisec.innerHTML = "00";
      timerSec.innerHTML = "000";
    //   timerMins.innerHTML = "00";
    //   timerHrs.innerHTML = "00";
      startBtn.innerHTML = "Start";
      lapRecord.innerHTML = '';
      status = "stopped";
    }
    
    function lap() {
      stepNum++
      lapNow = `<div class="lap">${seconds} : ${stepNum} </div>`;
      // xarray.push(toString(seconds))
      lapRecord.innerHTML += lapNow;
      xarray.push(seconds+(miliseconds/100))
      x = xarray.join(',');
      
      // document.getElementById('id_element'+ stepNum).value = `${seconds}`;
    //   if (stepNum == 1) {
      document.getElementById('id_steptime_1').value = xarray[0].toFixed(2);
      document.getElementById('id_steptime_2').value = (xarray[1] - xarray[0]).toFixed(2);
      document.getElementById('id_steptime_3').value = (xarray[2] - xarray[1]).toFixed(2);
      document.getElementById('id_steptime_4').value = (xarray[3] - xarray[2]).toFixed(2);
      document.getElementById('id_steptime_5').value = (xarray[4] - xarray[3]).toFixed(2);
      document.getElementById('id_steptime_6').value = (xarray[5] - xarray[4]).toFixed(2);
        // document.getElementById('id_steptime_7').value = (xarray[6] - xarray[5]).toFixed(2);
        // document.getElementById('id_steptime_8').value = (xarray[7] - xarray[6]).toFixed(2);
        // document.getElementById('id_steptime_9').value = (xarray[8] - xarray[7]).toFixed(2);
        // document.getElementById('id_steptime_10').value = (xarray[9] - xarray[8]).toFixed(2);
        // document.getElementById('id_steptime_11').value = (xarray[10] - xarray[9]).toFixed(2);
        // document.getElementById('id_steptime_12').value = (xarray[11] - xarray[10]).toFixed(2);
        // document.getElementById('id_steptime_13').value = (xarray[12] - xarray[11]).toFixed(2);
        // document.getElementById('id_steptime_14').value = (xarray[13] - xarray[12]).toFixed(2);
        // document.getElementById('id_steptime_15').value = (xarray[14] - xarray[13]).toFixed(2);
      
        if (xarray[0].toFixed(2) > 25.3 || xarray[0].toFixed(2) < 18.7 && stepNum == 1) {
            document.getElementById('id_checkstatus_1').value = false;
            stepadh++;
        }
        else if (stepNum == 1) {
            document.getElementById('id_checkstatus_1').value = true;
        };
        if ((xarray[1] - xarray[0]).toFixed(2) > 17.25 || (xarray[1] - xarray[0]).toFixed(2) < 12.75 && stepNum == 2) {
            document.getElementById('id_checkstatus_2').value = false;
            stepadh++;
        }   else if (stepNum == 2) {
            document.getElementById('id_checkstatus_2').value = true;
        };
        if ((xarray[2] - xarray[1]).toFixed(2) > 14.95 || (xarray[2] - xarray[1]).toFixed(2) < 11.05 && stepNum == 3) {
            document.getElementById('id_checkstatus_3').value = false;
            stepadh++;
        }   else if (stepNum == 3) {
            document.getElementById('id_checkstatus_3').value = true;
        };
        if ((xarray[3] - xarray[2]).toFixed(2) > 16.1 || (xarray[3] - xarray[2]).toFixed(2) < 11.9 && stepNum == 4) {
            document.getElementById('id_checkstatus_4').value = false;
            stepadh++;
        }   else if (stepNum == 4) {
            document.getElementById('id_checkstatus_4').value = true;
        };
        if ((xarray[4] - xarray[3]).toFixed(2) > 31.05 || (xarray[4] - xarray[3]).toFixed(2) < 14.95 && stepNum == 5) {
            document.getElementById('id_checkstatus_5').value = false;
            stepadh++;
        }   else if (stepNum == 5){
            document.getElementById('id_checkstatus_5').value = true;
        };
        if ((xarray[5] - xarray[4]).toFixed(2) > 21.85 || (xarray[5] - xarray[4]).toFixed(2) < 8.25 && stepNum == 6) {
            document.getElementById('id_checkstatus_6').value = false;
            stepadh++;
        }   else if (stepNum == 6) {
            document.getElementById('id_checkstatus_6').value = true;
        };
        
        

        // if ((xarray[6] - xarray[5]).toFixed(2) > 5.75 || (xarray[6] - xarray[5]).toFixed(2) < 4.25) {
        //     document.getElementById('id_checkstatus_7').value = false;
        // }   else {
        //     document.getElementById('id_checkstatus_7').value = true;
        // };
        // if ((xarray[7] - xarray[6]).toFixed(2) > 5.75 || (xarray[7] - xarray[6]).toFixed(2) < 4.25) {
        //     document.getElementById('id_checkstatus_8').value = false;
        // }   else {
        //     document.getElementById('id_checkstatus_8').value = true;
        // };
        // if ((xarray[8] - xarray[7]).toFixed(2) > 13.8 || (xarray[8] - xarray[7]).toFixed(2) < 10.2) {
        //     document.getElementById('id_checkstatus_9').value = false;
        // }   else {
        //     document.getElementById('id_checkstatus_9').value = true;
        // };
        // if ((xarray[9] - xarray[8]).toFixed(2) > 2.3 || (xarray[9] - xarray[8]).toFixed(2) < 1.7) {
        //     document.getElementById('id_checkstatus_10').value = false;
        // }   else {
        //     document.getElementById('id_checkstatus_10').value = true;
        // };
        // if ((xarray[10] - xarray[9]).toFixed(2) > 6.9 || (xarray[10] - xarray[9]).toFixed(2) < 5.1) {
        //     document.getElementById('id_checkstatus_11').value = false;
        // }   else {
        //     document.getElementById('id_checkstatus_11').value = true;
        // };
        // if ((xarray[11] - xarray[10]).toFixed(2) > 4.6 || (xarray[11] - xarray[10]).toFixed(2) < 3.4) {
        //     document.getElementById('id_checkstatus_12').value = false;
        // }   else {
        //     document.getElementById('id_checkstatus_12').value = true;
        // };
        // if ((xarray[12] - xarray[11]).toFixed(2) > 3.45 || (xarray[12] - xarray[11]).toFixed(2) < 2.55) {
        //     document.getElementById('id_checkstatus_13').value = false;
        // }   else {
        //     document.getElementById('id_checkstatus_13').value = true;
        // };
        // if ((xarray[13] - xarray[12]).toFixed(2) > 14.95 || (xarray[13] - xarray[12]).toFixed(2) < 11.05) {
        //     document.getElementById('id_checkstatus_14').value = false;
        // }   else {
        //     document.getElementById('id_checkstatus_14').value = true;
        // };
        // if ((xarray[14] - xarray[13]).toFixed(2) > 3.45 || (xarray[14] - xarray[13]).toFixed(2) < 2.55) {
        //     document.getElementById('id_checkstatus_15').value = false;
        // }   else {
        //     document.getElementById('id_checkstatus_15').value = true;
        // };





        // if ((xarray[2] - xarray[2]).toFixed(2) > 5.75 || (xarray[1] - xarray[0]).toFixed(2) < 4.25) {
        //     document.getElementById('id_checkstatus_3').value = false;
        // }   else {
        //     document.getElementById('id_checkstatus_3').value = true;
        // };
    //   //  block of code to be executed if the condition is true
    //   } else {
    //     document.getElementById('id_steptime_'+ stepNum).value = xarray[stepNum-1] - xarray[stepNum-2];
    //   }
      // document.getElementById('id_element1').value = xarray[0];
      // document.getElementById('id_element'+ stepNum).value = xarray[stepNum-1] - xarray[stepNum-2];
      
    //   stepRecord.innerHTML ++;
    document.getElementById('id_periodadh').value = (6-stepadh)/6;
    
    }
    
   
    
    
    lapBtn.addEventListener('click', lap);
    startBtn.addEventListener('click', startStop);
    resetBtn.addEventListener('click', reset);
    
    
