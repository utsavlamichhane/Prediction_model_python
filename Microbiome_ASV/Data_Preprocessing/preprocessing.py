
import pandas as pd


asv_df = pd.read_csv('Rumen_ASV_table_clean.csv')


asv_transposed = asv_df.set_index('ASV ID').T


asv_transposed = (
    asv_transposed
    .reset_index()
    .rename(columns={'index': 'SampleID'})
)




rfi_df = pd.read_excel('overall_RFI_only.xlsx')




merged = pd.merge(asv_transposed,
                  rfi_df,
                  on='SampleID',
                  how='left')


merged.to_csv('preprocessed_ASV_level_1.csv', index=False)

print("Saved transposed & merged file as 'preprocessed_ASV_level_1.csv'")


##lets look the preprocessed 1

df = preprocessed_1

print("Shape (rows × columns):", df.shape)
print("\nColumn names:")
print(df.columns.tolist())


print("\nHead (first 5 rows):")
print(df.head())


print("\nTail (last 5 rows):")
print(df.tail())


print("\nInfo:")
print(df.info())



####

df = pd.read_csv('preprocessed_ASV_level_1.csv')


cols = df.columns.tolist()
cols.remove('Overall_RFI')
new_order = cols[:1] + ['Overall_RFI'] + cols[1:]

df = df[new_order]


df.to_csv('preprocessed_ASV_level_2.csv', index=False)

print("Saved reordered file as 'preprocessed_ASV_level_2.csv'")




