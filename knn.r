tab <- read.csv("./knn_test_data/knn_scores.csv",header = FALSE)
colnames(tab) <- c ("1","5","9","13","17")
mat <- as.matrix(tab)
pdf("knn.pdf")
l <- c("Accuracy","Recall","Precision","F1-Measure")

barplot(mat, main ="Overall KNN Scores",col = c("aquamarine2","azure3","coral2","orchid3"),
        beside = TRUE, ylim =c(0.9,0.98), ylab = "Measured Score", xlab = "K",xpd=FALSE,border="white")
legend("topright", legend = l, 
       fill = c("aquamarine2","azure3","coral2","orchid3"), box.lty = 0.5, cex = 1,
)

dev.off()

