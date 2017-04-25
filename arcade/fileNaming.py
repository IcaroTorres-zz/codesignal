# poor but functional solution
def fileNaming(names):
    newArr = []
    for i in range(len(names)):
        count = 0
        tmp = names[i]

        if (''.join(newArr).find(names[i]) > -1):
            while (''.join(newArr).find(names[i]) > -1):

                count+=1
                if len(names[i])!=1:
                    names[i] = tmp + "(" + str(count) + ")"
                else:
                    names[i] = tmp+'*'

        newArr.append(names[i])
    for i,s in enumerate(newArr):
        newArr[i]=''.join(newArr[i]).replace('*','',len(newArr[i]))
    return newArr

# much beautiful solution
def fileNaming1(names):
    naming, s = [], set()

    for name in names:
        newName, c = name, 0

        while newName in s:
            c += 1
            newName = name + '(' + str(c) + ')'
        else:
            s.add(newName)
            naming.append(newName)

    return naming


# best solution
def fileNaming(names):
    for i in range(len(names)):
        if names[i] in names[:i]:
            j=1
            while names[i]+"("+str(j)+")" in names[:i]:
                j+=1
            names[i]+="("+str(j)+")"
    return names

A=["dd",  "dd(1)",  "dd(2)",  "dd",  "dd(1)",  "dd(1)(2)",  "dd(1)(1)", "dd",  "dd(1)"]
B=["doc", "doc", "image",  "doc(1)",  "doc"]
C=["a(1)",  "a(6)",  "a",  "a",  "a",  "a", "a",  "a",  "a",  "a",  "a",  "a"]
print fileNaming(C)

# JS
# function fileNaming(names) {
#     var newArr = [];
#     for (var i = 0; i < names.length; i++) {
#         var count = 0;
#         var tmp = names[i];
#         if (newArr.indexOf(names[i]) > -1) {
#             while (newArr.indexOf(names[i]) > -1) {
#                 count++;
#                 names[i] = tmp + "(" + count + ")";
#             }
#         }
#         newArr.push(names[i]);
#     }
#     return newArr;
# }
