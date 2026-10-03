"""Generated from Smithy shape ``com.amazonaws.machinelearning#RedshiftDatabaseUsername``."""

from typing import TypeAlias

"""<p>A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on an Amazon Redshift cluster. The username should have sufficient permissions to execute the <code>RedshiftSelectSqlQuery</code> query. The username should be valid for an Amazon Redshift <a href="https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html">USER</a>.</p>"""
RedshiftDatabaseUsername: TypeAlias = str
