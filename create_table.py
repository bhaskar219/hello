@st.composite
def table_strategy(draw):
    
    column_names = []
    columns = []
    for i in range(draw(st.integers(min_value=1, max_value=10))):
        column_name = 'c' + str(i + 1)
        column_type = draw(st.sampled_from(['INT', 'VARCHAR(255)', 'FLOAT']))
        not_null = draw(st.booleans())
        columns.append((column_name, column_type, not_null))
        column_names.append(column_name)
    primary_key_columns = [column_names[i] for i in range(len(column_names)) if column_names[i] and draw(st.booleans())]
    index_columns = random.sample(column_names, draw(st.integers(min_value=0, max_value=len(column_names))))
    unique_columns = random.sample(column_names, draw(st.integers(min_value=0, max_value=len(column_names))))
    foreign_key_columns = random.sample(column_names, draw(st.integers(min_value=0, max_value=len(column_names))))
    if foreign_key_columns:
        
        foreign_columns = []
        for column in foreign_key_columns:
            foreign_column_name = 'c' + str(random.randint(1, 100))
            while foreign_column_name in foreign_columns:
                foreign_column_name = 'c' + str(random.randint(1, 100))
            foreign_columns.append(foreign_column_name)
        foreign_table = next(fn_name)#'t' + str(random.randint(1, 100))
        foreign_key = (foreign_table, [column for column in foreign_key_columns], foreign_columns)
        create_foreign_table = True #draw(st.booleans())
    else:
        foreign_key = None
        create_foreign_table = False
    table_name = next(tab_name)#'t' + str(random.randint(1, 100))
    return (table_name, columns, primary_key_columns, index_columns, unique_columns, foreign_key, create_foreign_table)
