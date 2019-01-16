/*/
function getCountDay(startDate, endDate) {
    let days = (Math.round(endDate.getTime() - startDate.getTime()))/ (1000 * 60 * 60 * 24);
    days += 1;
    console.log('Count days: ', days);
    return days;
}

function getDaysBetweenDifferenceDate (dayOfWeek, startDate, endDate) {
    console.log(startDate);
    console.log(endDate);
    const startDay = startDate.getDay();
    const endDay = endDate.getDay();
    if (startDay > dayOfWeek) {
        startDate.setDate(startDate.getDate() + (7 - (startDay - dayOfWeek)));
    }
    if (endDay > dayOfWeek) {
        endDate.setDate(endDate.getDate() - (endDay - dayOfWeek))
    }
    console.log(startDate);
    console.log(endDate);
    const days = getCountDay(startDate, endDate);
    const countDayOfWeek = Math.floor(days/7) + 1;
    return countDayOfWeek;
}

const startD = new Date('01/23/2019');
const endD = new Date('01/24/2019');
const countMonday = getDaysBetweenDifferenceDate(1, startD, endD);
console.log(countMonday); 

/*/
function count(dayOfWeek, startDay, endDay) {
    console.log(startDay, startDay.getDay());
    console.log(endDay, endDay.getDay());
    const numOfDays = 1 + Math.round((endDay - startDay) / (24 * 3600 * 1000));
    return Math.floor((numOfDays + (startDay.getDay() + 6 - dayOfWeek) % 7 ) / 7 );
}
  
console.log(count(1, new Date(2019, 0, 12), new Date(2019, 0, 13)));
console.log(count(1, new Date(2019, 0, 13), new Date(2019, 0, 14)));
console.log(count(1, new Date(2019, 0, 14), new Date(2019, 0, 15)));
console.log(count(1, new Date(2019, 0, 15), new Date(2019, 0, 16)));
//*/
