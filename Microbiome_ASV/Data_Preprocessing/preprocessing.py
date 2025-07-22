
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


##
