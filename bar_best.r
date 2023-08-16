tab <- read.csv("best_scores.csv",header = FALSE)
transposed <- t(tab)
colnames(transposed) <- c ("KNN - 1","BDT Depth - 12", "Liblinear Alpha - 0.0001")
mat <- as.matrix(transposed)

pdf("./graphs/selected_bar.pdf")
l <- c("Accuracy","Recall","Precision","F1-Measure","Specificity")

barplot(mat, main ="Overall Best Scores",col = c("aquamarine2","azure3","coral2","orchid3","black"),
        beside = TRUE, ylim =c(0.9,0.98), ylab = "Score", xlab = "Model",xpd=FALSE,border="white")
legend("topright", legend = l, 
       fill = c("aquamarine2","azure3","coral2","orchid3","black"), box.lty = 0.5, cex = 1,
)

dev.off()

boxbest <- read.csv("box.csv",header = FALSE)
boxplot(boxbest,xlab="Model",xaxt='n',ylab="Score",ylim=c(0.92,1), main="Box Plot Precision",col="azure3")
axis(1, at=1:3, labels=c("KNN - 1","BDT Depth - 12", "Alpha - 0.0001"))

