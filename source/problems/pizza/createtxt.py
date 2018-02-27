from scipy import io as scio


mat_content = scio.loadmat("medium2.mat")['slices']

f = open("sol.txt", "w")
f.write(str(len(mat_content))+"\n")
for slice in mat_content:
    f.write(str(slice[0][0])+" "+str(slice[0][1])+" "+str(slice[1][0])+" "+str(slice[1][1])+"\n")