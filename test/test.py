"""Tests for pytaxize"""

import os
import pytaxize

# expected results
exp1 = {
 u'canonical_form': u'Helianthus annus',
 u'classification_path': u'',
 u'classification_path_ids': u'',
 u'classification_path_ranks': u'',
 u'data_source_id': 12,
 u'data_source_title': u'EOL',
 u'edit_distance': 0,
 u'gni_uuid': u'f5674e32-00cc-57e3-b632-6a0b89fa4df4',
 u'local_id': u'468106',
 u'match_type': 1,
 u'name_string': u'Helianthus annus',
 u'prescore': u'3|0|0',
 u'score': 0.988,
 u'taxon_id': u's_5106367',
 u'url': u'http://eol.org/pages/468106/names/synonyms'
}

def test_gnr_resolve():
    """Basic test of of gnr_resolve"""
    assert exp1 == pytaxize.gnr_resolve('Helianthus annus')[0][0]

# def test_auto_get_columns_cleanup():
#     """Test of automatically cleaning up column labels from header"""
#     test_engine.table.delimiter = ","
#     columns, column_values = test_engine.table.auto_get_columns("a),b.b,c/c,d___d,group")
#     assert columns == [['a', None], ['b_b', None], ['c_c', None], ['d_d', None],
#                        ['grp', None]]


# def test_auto_get_delimiter_comma():
#     """Test if commas are properly detected as delimiter"""
#     test_engine.auto_get_delimiter("a,b,c;,d")
#     assert test_engine.table.delimiter == ","


# def test_auto_get_delimiter_tab():
#     """Test if commas are properly detected as delimiter"""
#     test_engine.auto_get_delimiter("a\tb\tc\td,")
#     assert test_engine.table.delimiter == "\t"


# def test_auto_get_delimiter_semicolon():
#     """Test if semicolons are properly detected as delimiter"""
#     test_engine.auto_get_delimiter("a;b;c;,d")
#     assert test_engine.table.delimiter == ";"


# def test_create_db_statement():
#     """Test creating the create database SQL statement"""
#     assert test_engine.create_db_statement() == 'CREATE DATABASE test_abc'


# def test_database_name():
#     """Test creating database name"""
#     assert test_engine.database_name() == 'test_abc'


# def test_drop_statement():
#     "Test the creation of drop statements"
#     assert test_engine.drop_statement('TABLE', 'tablename') == "DROP TABLE IF EXISTS tablename"


# def test_escape_single_quotes():
#     """Test escaping of single quotes"""
#     assert test_engine.escape_single_quotes("1,2,3,'a'") == "1,2,3,\\'a\\'"


# def test_escape_double_quotes():
#     """Test escaping of double quotes"""
#     assert test_engine.escape_double_quotes('"a",1,2,3') == '\\"a\\",1,2,3'


# def test_extract_values():
#     """Test extraction of values from line of data with already know delimiter"""
#     test_engine.table.delimiter = ","
#     assert test_engine.table.extract_values('abcd,1,2,3.3') == ['abcd', '1', '2', '3.3']


# def test_extract_values_fixed_width():
#     """Test extraction of values from line of fixed width data"""
#     test_engine.table.fixed_width = [5, 2, 2, 3, 4]
#     assert test_engine.table.extract_values('abc  1 2 3  def ') == ['abc', '1', '2', '3', 'def']


# def test_find_file_absent():
#     """Test if find_file() properly returns false if no file is present"""
#     assert test_engine.find_file('missingfile.txt') is False


# def test_find_file_present():
#     """Test if existing datafile is found
#     Using the AvianBodySize dataset which is included for regression testing
#     Because all testing code and data is located in ./test/ it is necessary to
#     move into this directory for DATA_SEARCH_PATHS to work properly.
#     """
#     test_engine.script.shortname = 'AvianBodySize'
#     os.chdir('./test/')
#     assert test_engine.find_file('avian_ssd_jan07.txt') == 'raw_data/AvianBodySize/avian_ssd_jan07.txt'
#     os.chdir('..')


# def test_format_data_dir():
#     "Test if directory for storing data is properly formated"
#     test_engine.script.shortname = "TestName"
#     assert test_engine.format_data_dir() == os.path.join(HOMEDIR,
#                                                          '.retriever/raw_data/TestName')

# def test_format_filename():
#     "Test if filenames for stored files are properly formated"
#     test_engine.script.shortname = "TestName"
#     assert test_engine.format_filename('testfile.csv') == os.path.join(HOMEDIR, '.retriever/raw_data/TestName/testfile.csv')


# def test_format_insert_value_int():
#     """Test formatting of values for insert statements"""
#     assert test_engine.format_insert_value(42, 'int') == 42


# def test_format_insert_value_double():
#     """Test formatting of values for insert statements"""
#     assert test_engine.format_insert_value(26.22, 'double') == '26.22'


# def test_format_insert_value_string_simple():
#     """Test formatting of values for insert statements"""
#     assert test_engine.format_insert_value('simple text', 'char') == "'simple text'"


# def test_format_insert_value_string_complex():
#     """Test formatting of values for insert statements"""
#     assert test_engine.format_insert_value('my notes: "have extra, stuff"', 'char') == '\'my notes: \\"have extra, stuff\\"\''
