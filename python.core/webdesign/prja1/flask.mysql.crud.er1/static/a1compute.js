function compute(){
    var m1=0,m2=0,total=0,avg=0,result='fail'
    m1 = parseFloat(numm1.value);
    m1 = isNaN(m1) ? 0 : m1;
    m2 = parseFloat(numm2.value);
    m2 = isNaN(m2) ? 0 : m2;
    total = m1 + m2;
    avg = total / 2;
    result = (m1 > 34.4 && m2 > 34.4) ? 'pass' : 'fail';
    numtotal.value = total.toFixed(2);
    numavg.value = avg.toFixed(2);
    tbxresult.value = result;
}