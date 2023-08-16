pdf("./graphs/Decision_Tree_Scores.pdf")
scores_tree <- read.csv("./tree_test_data/tree_scores.log", header=FALSE)
plot(scores_tree$V1, scores_tree$V2,ylab="Score" ,xlab="Tree Depth", 
     main="Decision Tree Mean Scores",type="l",col="aquamarine2",ylim=c(0.5,1),lwd=2.0) #Accuracy
lines(scores_tree$V4, type = "l", col="azure3",lwd=2.0) #Recall
lines(scores_tree$V6, type = "l", col="coral2",lwd=2.0) #Precision
lines(scores_tree$V8, type = "l", col="orchid3",lwd=2.0) #F1-Measure
lines(scores_tree$V10, type = "l", col="black",lwd=2.0) #Specificity
legend("bottomright", legend=c("Accuracy","Recall","Precision","F1-Measure","Specificity"),
       col = c("aquamarine2","azure3","coral2","orchid3","black"), lty = c( 1,1,1,1,1), 
cex=0.8
)
dev.off()

pdf("./graphs/KNN_Scores.pdf")
scores_knn <- read.csv("./knn_test_data/knn_scores.log", header=FALSE)
plot(scores_knn$V1, scores_knn$V2,ylab="Score",ylim=c(0.9,0.98) ,xlab="K", 
     main="KNN Mean Scores",type="l",col="aquamarine2",lwd=2.0) #Accuracy
lines(scores_knn$V1, scores_knn$V4, type = "l", col="azure3",lwd=2.0) #Recall
lines(scores_knn$V1, scores_knn$V6, type = "l", col="coral2",lwd=2.0) #Precision
lines(scores_knn$V1, scores_knn$V8, type = "l", col="orchid3",lwd=2.0) #F1-Measure
lines(scores_knn$V1, scores_knn$V10, type = "l", col="black",lwd=2.0) #Specificity
legend("bottomright", legend=c("Accuracy","Recall","Precision","F1-Measure","Specificity"),
       col = c("aquamarine2","azure3","coral2","orchid3","black"), lty = c( 1,1,1,1,1), 
       cex=0.8
)
dev.off()

pdf("./graphs/Regression_Scores_lbfgs.pdf")
scores_regression_lbfgs <- read.csv("./regression_test_data/regression_scores_lbfgs.log", header=FALSE)
plot(scores_regression_lbfgs$V3,ylab="Score", xlab="Alpha",xaxt="n",ylim =c(0.85,0.96), 
     main="Regression Mean Scores Using Lbfgs",type="l",col="aquamarine2",lwd=2.0) #Accuracy
axis(1, at=1:5, labels=c("1","0.1","0.01","0.001","0.0001"))
lines(scores_regression_lbfgs$V5, type = "l", col="azure3",lwd=2.0) #Recall
lines(scores_regression_lbfgs$V7, type = "l", col="coral2",lwd=2.0) #Precision
lines(scores_regression_lbfgs$V9, type = "l", col="orchid3",lwd=2.0) #F1-Measure
lines(scores_regression_lbfgs$V11, type = "l", col="black",lwd=2.0) #Specificity
legend("bottomright", legend=c("Accuracy","Recall","Precision","F1-Measure","Specificity"),
       col = c("aquamarine2","azure3","coral2","orchid3","black"), lty = c( 1,1,1,1,1), 
       cex=0.8
)
dev.off()

pdf("./graphs/Regression_Scores_liblinear.pdf")
scores_regression_liblinear <- read.csv("./regression_test_data/regression_scores_liblinear.log", header=FALSE)
plot(scores_regression_liblinear$V3,ylab="Score", xlab="Alpha",xaxt="n",ylim =c(0.85,0.96), 
     main="Regression Mean Scores Using Liblinear",type="l",col="aquamarine2",lwd=2.0) #Accuracy
axis(1, at=1:5, labels=c("1","0.1","0.01","0.001","0.0001"))
lines(scores_regression_liblinear$V5, type = "l", col="azure3",lwd=2.0) #Recall
lines(scores_regression_liblinear$V7, type = "l", col="coral2",lwd=2.0) #Precision
lines(scores_regression_liblinear$V9, type = "l", col="orchid3",lwd=2.0) #F1-Measure
lines(scores_regression_liblinear$V11, type = "l", col="black",lwd=2.0) #Specificity
legend("bottomright", legend=c("Accuracy","Recall","Precision","F1-Measure","Specificity"),
       col = c("aquamarine2","azure3","coral2","orchid3","black"), lty = c( 1,1,1,1,1), 
       cex=0.8
)
dev.off()

