library(randomForest) 
files = list.files(path="csv\\san",pattern="f.csv", full.names = TRUE)
lapply(files, function(x){
input=read.csv(file=x,sep = ",",header = TRUE)

rf1=randomForest(input[,-1],input[,1], ntree = 50)
rf1
})
lapply(files, function(x){
  input=read.csv(file=x,sep = ",",header = TRUE)
  
  rf1=randomForest(input[,-1],input[,1], ntree = 50)
  importance(rf1)
})
files = list.files(path="csv\\raw",pattern="f.csv", full.names = TRUE)
lapply(files, function(x){
input=read.csv(file=x,sep = ",",header = TRUE)

rf2=randomForest(input[,-1],input[,1], ntree = 50)
rf2 
}) 