setwd("E:/SCHOOLWORK/CSU Global/MIS581 Capstone")
library(dplyr)
library(ggpubr)
library(lubridate)
library(tree)
library(rpart)
library(rpart.plot)

df <- read.csv("Superstore Dataset 2.csv", header=TRUE)

#DOES DISCOUNT IMPACT PROFIT? 

#Creating New Conditional Row
df$DiscountYes <- ifelse(df$Discount > 0, 0, 1)

#Viewing box plots of profit for discounted vs. not discounted
ggboxplot(df, x = "DiscountYes", y = "Profit", 
          color = "DiscountYes", palette = c("#00AFBB", "#E7B800"),
          ylab = "Profit", xlab = "Discount")

#Subsetting into Yes and No
dcyes <- subset(df, df$DiscountYes == 1, select=c(DiscountYes,Profit))
dcno <- subset(df, df$DiscountYes == 0, select=c(DiscountYes,Profit))

#t-test
dctest <- t.test(dcyes$Profit, dcno$Profit, var.equal=TRUE)
dctest



#DOES SHIPPING TIME AFFECT PROFITS?

#Converting values to dates
#df$Order.Date <- as.Date(df$Order.Date, format = "%m/%d/%Y")
df$Order.Date = parse_date_time(df$Order.Date, c("%d/%m/%Y", "%m-%d-%Y", "%d-%m-%Y"))
#df$Ship.Date <- as.Date(df$Ship.Date, format= "%m/%d/%Y")
df$Ship.Date = parse_date_time(df$Ship.Date, c("%d/%m/%Y", "%m-%d-%Y", "%d-%m-%Y"))

#finding the time between order -> ship; then converting to numeric
df <- df %>% mutate(ShipTime = Ship.Date - Order.Date)
df$ShipTime <- as.numeric(df$ShipTime, units="days")

#subsetting into high & low shipping times
lowship <- subset(df, df$ShipTime <= 2, select=c(ShipTime, Profit))
highship <- subset(df, df$ShipTime >= 6, select=c(ShipTime, Profit))

#two-sample t-test
shiptest <- t.test(lowship$Profit, highship$Profit, var.equal=FALSE)
shiptest





#DOES THE SEGMENT OF CUSTOMER IMPACT PROFIT?

#convert profit into binary value - gain or loss


#segment into tree categories
treedf <- subset(df, select=c(Profit, Ship.Mode, Segment, Market, Category, ShipTime, NetGain))
#treedf$NetGain = cut(treedf$NetGain, 2, labels=c('Loss', 'Gain'))
set.seed(1234)
ind <- sample(2, nrow(treedf), replace = T, prob = c(0.6, 0.4)) #train/test


treedf$NetGain <- ifelse(df$Profit >0, 1, 0)
#treedf$NetGain <- cut(df$Profit, 7, labels=c('-3', '-2', '-1', '0', '1', '2', '3'))

ttrain <- treedf[ind==1,] #partitioning
ttest <- treedf[ind==2,]

tree <- rpart(NetGain ~ ., data=treedf, minsplit = 4)  #tree



#ATTEMPT 2:  T-TEST WITH FILTERED SAMPLES OF HIGH/LWO PROFIT
summary(df$Profit)
#preparing for two-set t-test by converting segment to a numerical value
#1 = home office    #2 = corporate    #3 = consumer 
#$Segment <- sapply(as.character(x), switch, "Home Office" = 1, 
                     #"Corporate" = 2, "Consumer" = 3, USE.NAMES=F)

consumer <-subset(df, df$Segment =="Consumer", select=c(Segment, Profit))
homeoffice <-subset(df, df$Segment == "Home Office", select=c(Segment, Profit))

#writing to new csv files to analyze in tableau
#write.csv(highprof, "E:/SCHOOLWORK/CSU Global/MIS581 Capstone\\highprof.csv", row.names=FALSE)
#write.csv(lowprof, "E:/SCHOOLWORK/CSU Global/MIS581 Capstone\\lowprof.csv", row.names=FALSE)

