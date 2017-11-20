import matplotlib.pyplot as plt

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=70,
        shadow= True,
        explode=(0,0,0.2,0),
        autopct='%1.1f%%')

plt.title('Interesting Graph\nCheck it out')
plt.show()