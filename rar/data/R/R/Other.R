dev.new(width=10, height=6.5)
split.screen(c(1, 2))
x <- read.csv("Scat1.txt",header=T,sep="\t")
x <- t(x)
DNets <- as.numeric(x[1,0:69])
TotWL <- as.numeric(x[2,0:69])
MaxWL <- as.numeric(x[3,0:69])

screen(1)
scatterplot3d(DNets, TotWL, MaxWL,
angle=35, grid=TRUE,
xlim = c(0, 100), ylim = c(0, 100), zlim = c(0, 100))

x <- read.csv("Scat2_2.txt",header=T,sep="\t")
x <- t(x)
d <- as.numeric(x[1,0:14])
e <- as.numeric(x[2,0:14])
f <- as.numeric(x[3,0:14])
screen(2)
scatterplot3d(d, e, f, pch = 16, color="red", angle=35, grid=TRUE,
label.tick.marks=FALSE,
xlim = c(0, 100), ylim = c(0, 100), zlim = c(0, 100))