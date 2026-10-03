"""Generated from Smithy shape ``com.amazonaws.machinelearning#RedshiftDatabasePassword``."""

from typing import TypeAlias

"""<p>A password to be used by Amazon ML to connect to a database on an Amazon Redshift cluster. The password should have sufficient permissions to execute a <code>RedshiftSelectSqlQuery</code> query. The password should be valid for an Amazon Redshift <a href="https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html">USER</a>.</p>"""
RedshiftDatabasePassword: TypeAlias = str
