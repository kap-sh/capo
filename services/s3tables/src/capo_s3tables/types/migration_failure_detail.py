"""Generated from Smithy shape ``com.amazonaws.s3tables#MigrationFailureDetail``."""

from typing import TypeAlias

"""<p>The resource that the failure applies to, such as the role ARN, the Amazon Web Services Glue table (<code>database.table</code>) or a bucket. For <code>sourceNotSupported</code>, the reason that the source isn't supported.</p>"""
MigrationFailureDetail: TypeAlias = str
