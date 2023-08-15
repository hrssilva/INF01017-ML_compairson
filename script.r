df <- data.frame(read.csv("./dataset/Phishing_Legitimate_full.csv"))
norm <- data.frame(matrix(nrow = 0, ncol = 0)) 
norm
x <- 1
y <- 1
l <- length(df)
r <- nrow(df)

max(df[1])
max(df[2])
max(df[3])

while (x <= length(df)) {
  while (y <= nrow(df)) {
    norm[y,3] = 10
    y <- y + 1
  }
  y <- 0
  x <- x + 1
}

df

