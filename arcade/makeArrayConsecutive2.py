def makeArrayConsecutive2(statues):
    statues = sorted(statues)
    result = 0
    for i in range (0,len(statues)-1):
        result = result + statues[i+1]-statues[i]-1
    return result

'''
#JS
function makeArrayConsecutive2(statues) {
    statues=statues.sort((a,b)=> a > b ? 1 : a < b ? -1 : 0);
    var result = 0;
    for (var i =0; i< statues.length-1; i++ )
        result = result + statues[i+1]-statues[i]-1;
    return result;
}

#CS
int makeArrayConsecutive2(int[] statues) {
    Array.Sort(statues);
    int result = 0;
    for (int i =0; i< statues.Length-1; i++ )
        result = result + statues[i+1]-statues[i]-1;
    return result;
}

#JAVA
int makeArrayConsecutive2(int[] statues) {
    Arrays.sort(statues);
    int result = 0;
    for (int i =0; i< statues.length-1; i++ )
        result = result + statues[i+1]-statues[i]-1;
    return result;
}
