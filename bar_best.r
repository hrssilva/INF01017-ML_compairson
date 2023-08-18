tab <- read.csv("best_scores.csv",header = FALSE)
transposed <- t(tab)
colnames(transposed) <- c ("KNN - 1","BDT Depth - 11", "Liblinear Alpha - 0.01")
mat <- as.matrix(transposed)

pdf("./graphs/selected_bar.pdf")
l <- c("Accuracy","Recall","Precision","F1-Measure","Specificity")

barplot(mat, main ="Overall Best Scores",col = c("aquamarine2","azure3","coral2","orchid3","black"),
        beside = TRUE, ylim =c(0.88,0.98), ylab = "Mean Score", xlab = "Model",xpd=FALSE,border="white")
legend("topright", legend = l, 
       fill = c("aquamarine2","azure3","coral2","orchid3","black"), box.lty = 0.5, cex = 1,
)

dev.off()

pdf("./graphs/selected_box_acc.pdf")
boxbest <- read.csv("box_acc.csv",header = FALSE)
boxplot(boxbest,xlab="Model",xaxt='n',ylab="Accuracy",ylim=c(0.90,1), main="Box Plot Accuracy",col="aquamarine2")
axis(1, at=1:3, labels=c("KNN - 1","BDT Depth - 11", "Alpha - 0.01"))
dev.off()

pdf("./graphs/selected_box_rec.pdf")
boxbest <- read.csv("box_rec.csv",header = FALSE)
boxplot(boxbest,xlab="Model",xaxt='n',ylab="Recall",ylim=c(0.90,1), main="Box Plot Precision",col="azure3")
axis(1, at=1:3, labels=c("KNN - 1","BDT Depth - 11", "Alpha - 0.01"))
dev.off()
