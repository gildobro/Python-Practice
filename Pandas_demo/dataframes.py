import pandas

df1 = pandas.DataFrame([[2,4,6],[10,20,30]], 
columns=["Price","Age","Value"], 
index=["First","Second"])

#Dataframes using dictionaries
df2 = pandas.DataFrame([{"Name":"John","Sirname":"Deer"},{"Name":"Gil","Sirname":"Dobrovinsky"}])


#prints the data in a table
print(df1)
#prints the mean between the data in the data frame
print(df1.mean())
#prints the average of the averages of the data
print(df1.mean().mean())
#prints the datatype of the dataframe
print(type(df1.mean()))
#prints individual column data
print(df1.Age)
#prints individual column data and its average
print(df1.Price.mean())
#prints df2 which defines two dictionaries with Name, and Sirname
print(df2)
