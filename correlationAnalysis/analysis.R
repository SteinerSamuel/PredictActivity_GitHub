# This R file contains the the correlation analysis of the Data collected from the
# GitHub API. This is to make sure we arent looking at features which are too corellated
# correlation set at 0.7 
library(readr)
library(Hmisc)
library(dendextend)

# Loads in the data
result <- read_delim("result.csv", "\t",escape_double = FALSE, trim_ws = TRUE)

#gets the labels on their own
repository_label <- result$Repository
status_label <- result$Status

# removes the labels from the dataframe
result <-  result[,3:106]
res.matrix <- data.matrix(result)

# Does a correlation analysis based on the spearman rho function
rc <- rcorr(as.matrix(result), type="spearman")

# creates a heatmap of the correlation
col<- colorRampPalette(c("blue", "white", "red"))(200)
heatmap(x = rc$r, col = col, symm = TRUE)

# makes a dendrograh of the spearman rho function
v <- varclus(data.matrix(result),similarity = "spearman",trans = "square")
plot(v, cex = .6)

# grabs the dendrogrpah and returns a list of the the non removed features 
v.dendro <- as.dendrogram(v$hclust)

max <- as.integer(nleaves(v.d.cut$upper))
label.list <- list()
for (i in 1:max){
  label.list[[i]] <- as.character(labels(v.d.cut$lower[[i]])[1])
  print(labels(v.d.cut$lower[[i]])[1])
}
# creates a text file with the column names of the non removed features
lapply(label.list, write, "non_removed.txt", append=TRUE, ncolumns=1000)

# Creates the final dendrograph of the non removed  features
dendro <- v.d.cut$upper %>% set("labels",label.list)
dendro <- hang.dendrogram(dendro, hang = -1)
plot(dendro)

grep(paste(label.list, collapse='|') , names(result) )