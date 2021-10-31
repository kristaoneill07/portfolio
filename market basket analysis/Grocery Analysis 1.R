#libraries
library(lubridate)
library(tidyverse)
library(arules)
library(arulesViz)
library(datasets)
library(plyr)
library(RColorBrewer)


groc <- read.csv('Groceries_dataset.csv', head=TRUE)

#Initial viewing of top 10 and bottom 10 sales
counts <- dplyr::count(groc, groc$itemDescription, sort=TRUE)
names(counts)[1]<- 'itemDescription'
topten <- head(counts, 10)
lowten <- tail(counts, 10)

#plotting
barplot(height=topten$n, names=topten$itemDescription, horiz=T, las=1, main="Top 10 Sales")
barplot(height=lowten$n, names=lowten$itemDescription, horiz=T, las=1, main="Bottom 10 Sales")

#prep for apriori
groc_sorted <- groc[order(groc$Member_number),]
#ensuring that member_number is numerical 
groc_sorted$Member_number <- as.numeric(groc_sorted$Member_number)


##Combining into transactions by date
groc_list <- ddply(groc_sorted, c("Member_number", "Date"), function(groc_sorted)paste(groc_sorted$itemDescription, collapse=","))

#Results
head(groc_list,10)

#Removing member # and date
groc_list <- groc_list[-c(1,2)]
colnames(groc_list) <- c("items")

#Write to new csv
write.csv(groc_list, "grocerylist.csv", quote=FALSE, row.names=FALSE)

#import as transactions
transactions <- read.transactions(file="grocerylist.csv", rm.duplicates=TRUE, format="basket", sep=",",skip=1)
transactions@itemInfo$labels <- gsub("\"","",transactions@itemInfo$labels)


#inspecting data; inspecting frequencies
#inspect the top 10 to make sure it's good
inspect(head(transactions, 10))
summary(transactions)
itemFrequencyPlot(transactions,topN=20,type="absolute",col=brewer.pal(6,'Pastel2'), main="Absolute Item Frequency")

##Inspect frequent items
frequent <- eclat(transactions, parameter=list(supp = 0.05, maxlen=10))

inspect(frequent)


#a priori
rules = apriori(transactions, parameter = list(sup=0.001, conf=0.08, minlen=2, maxlen=2, target="rules"))
rules <- sort(rules, by="lift")
inspect(head(rules,10))
