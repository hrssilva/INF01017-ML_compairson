acc <- read.csv("./tree_test_data/acc.csv", header=FALSE)
plot(acc,ylab="Accuracy" ,xlab="Tree Depth", main="Decision Tree Accuracy",type="p",pch=19)

roc <- read.csv("./tree_test_data/roc.csv")