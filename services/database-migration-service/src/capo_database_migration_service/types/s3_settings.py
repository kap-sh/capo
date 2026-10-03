"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#S3Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.canned_acl_for_objects_value
    import capo_database_migration_service.types.compression_type_value
    import capo_database_migration_service.types.data_format_value
    import capo_database_migration_service.types.date_partition_delimiter_value
    import capo_database_migration_service.types.date_partition_sequence_value
    import capo_database_migration_service.types.encoding_type_value
    import capo_database_migration_service.types.encryption_mode_value
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.parquet_version_value
    import capo_database_migration_service.types.string


class S3Settings(TypedDict, closed=True):
    service_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p> The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the <code>iam:PassRole</code> action. It is a required parameter that enables DMS to write and read objects from an S3 bucket.</p>"""
    external_table_definition: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p> Specifies how tables are defined in the S3 source files only. </p>"""
    csv_row_delimiter: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    r"""<p> The delimiter used to separate rows in the .csv file for both source and target. The default is a carriage return (<code>\n</code>). </p>"""
    csv_delimiter: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> The delimiter used to separate columns in the .csv file for both source and target. The default is a comma. </p>"""
    bucket_folder: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> An optional parameter to set a folder name in the S3 bucket. If provided, tables are created in the path <code> <i>bucketFolder</i>/<i>schema_name</i>/<i>table_name</i>/</code>. If this parameter isn't specified, then the path used is <code> <i>schema_name</i>/<i>table_name</i>/</code>. </p>"""
    bucket_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> The name of the S3 bucket. </p>"""
    compression_type: NotRequired[
        "capo_database_migration_service.types.compression_type_value.CompressionTypeValue"
    ]
    """<p>An optional parameter to use GZIP to compress the target files. Set to GZIP to compress the target files. Either set this parameter to NONE (the default) or don't use it to leave the files uncompressed. This parameter applies to both .csv and .parquet file formats. </p>"""
    encryption_mode: NotRequired[
        "capo_database_migration_service.types.encryption_mode_value.EncryptionModeValue"
    ]
    """<p>The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either <code>SSE_S3</code> (the default) or <code>SSE_KMS</code>. </p> <note> <p>For the <code>ModifyEndpoint</code> operation, you can change the existing value of the <code>EncryptionMode</code> parameter from <code>SSE_KMS</code> to <code>SSE_S3</code>. But you can’t change the existing value from <code>SSE_S3</code> to <code>SSE_KMS</code>.</p> </note> <p>To use <code>SSE_S3</code>, you need an Identity and Access Management (IAM) role with permission to allow <code>"arn:aws:s3:::dms-*"</code> to use the following actions:</p> <ul> <li> <p> <code>s3:CreateBucket</code> </p> </li> <li> <p> <code>s3:ListBucket</code> </p> </li> <li> <p> <code>s3:DeleteBucket</code> </p> </li> <li> <p> <code>s3:GetBucketLocation</code> </p> </li> <li> <p> <code>s3:GetObject</code> </p> </li> <li> <p> <code>s3:PutObject</code> </p> </li> <li> <p> <code>s3:DeleteObject</code> </p> </li> <li> <p> <code>s3:GetObjectVersion</code> </p> </li> <li> <p> <code>s3:GetBucketPolicy</code> </p> </li> <li> <p> <code>s3:PutBucketPolicy</code> </p> </li> <li> <p> <code>s3:DeleteBucketPolicy</code> </p> </li> </ul>"""
    server_side_encryption_kms_key_id: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>If you are using <code>SSE_KMS</code> for the <code>EncryptionMode</code>, provide the KMS key ID. The key that you use needs an attached policy that enables Identity and Access Management (IAM) user permissions and allows use of the key.</p> <p>Here is a CLI example: <code>aws dms create-endpoint --endpoint-identifier <i>value</i> --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn=<i>value</i>,BucketFolder=<i>value</i>,BucketName=<i>value</i>,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=<i>value</i> </code> </p>"""
    data_format: NotRequired[
        "capo_database_migration_service.types.data_format_value.DataFormatValue"
    ]
    """<p>The format of the data that you want to use for output. You can choose one of the following: </p> <ul> <li> <p> <code>csv</code> : This is a row-based file format with comma-separated values (.csv). </p> </li> <li> <p> <code>parquet</code> : Apache Parquet (.parquet) is a columnar storage file format that features efficient compression and provides faster query response. </p> </li> </ul>"""
    encoding_type: NotRequired[
        "capo_database_migration_service.types.encoding_type_value.EncodingTypeValue"
    ]
    """<p>The type of encoding you are using: </p> <ul> <li> <p> <code>RLE_DICTIONARY</code> uses a combination of bit-packing and run-length encoding to store repeated values more efficiently. This is the default.</p> </li> <li> <p> <code>PLAIN</code> doesn't use encoding at all. Values are stored as they are.</p> </li> <li> <p> <code>PLAIN_DICTIONARY</code> builds a dictionary of the values encountered in a given column. The dictionary is stored in a dictionary page for each column chunk.</p> </li> </ul>"""
    dict_page_size_limit: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum size of an encoded dictionary page of a column. If the dictionary page exceeds this, this column is stored using an encoding type of <code>PLAIN</code>. This parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it reverts to <code>PLAIN</code> encoding. This size is used for .parquet file format only. </p>"""
    row_group_length: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of rows in a row group. A smaller row group size provides faster reads. But as the number of row groups grows, the slower writes become. This parameter defaults to 10,000 rows. This number is used for .parquet file format only. </p> <p>If you choose a value larger than the maximum, <code>RowGroupLength</code> is set to the max row group length in bytes (64 * 1024 * 1024). </p>"""
    data_page_size: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB). This number is used for .parquet file format only. </p>"""
    parquet_version: NotRequired[
        "capo_database_migration_service.types.parquet_version_value.ParquetVersionValue"
    ]
    """<p>The version of the Apache Parquet format that you want to use: <code>parquet_1_0</code> (the default) or <code>parquet_2_0</code>.</p>"""
    enable_statistics: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that enables statistics for Parquet pages and row groups. Choose <code>true</code> to enable statistics, <code>false</code> to disable. Statistics include <code>NULL</code>, <code>DISTINCT</code>, <code>MAX</code>, and <code>MIN</code> values. This parameter defaults to <code>true</code>. This value is used for .parquet file format only.</p>"""
    include_op_for_full_load: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that enables a full load to write INSERT operations to the comma-separated value (.csv) or .parquet output files only to indicate how the rows were added to the source database.</p> <note> <p>DMS supports the <code>IncludeOpForFullLoad</code> parameter in versions 3.1.4 and later.</p> <p>DMS supports the use of the .parquet files with the <code>IncludeOpForFullLoad</code> parameter in versions 3.4.7 and later.</p> </note> <p>For full load, records can only be inserted. By default (the <code>false</code> setting), no information is recorded in these output files for a full load to indicate that the rows were inserted at the source database. If <code>IncludeOpForFullLoad</code> is set to <code>true</code> or <code>y</code>, the INSERT is recorded as an I annotation in the first field of the .csv file. This allows the format of your target records from a full load to be consistent with the target records from a CDC load.</p> <note> <p>This setting works together with the <code>CdcInsertsOnly</code> and the <code>CdcInsertsAndUpdates</code> parameters for output to .csv files only. For more information about how these settings work together, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps">Indicating Source DB Operations in Migrated S3 Data</a> in the <i>Database Migration Service User Guide.</i>.</p> </note>"""
    cdc_inserts_only: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that enables a change data capture (CDC) load to write only INSERT operations to .csv or columnar storage (.parquet) output files. By default (the <code>false</code> setting), the first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated, or deleted at the source database for a CDC load to the target.</p> <p>If <code>CdcInsertsOnly</code> is set to <code>true</code> or <code>y</code>, only INSERTs from the source database are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are recorded depends on the value of <code>IncludeOpForFullLoad</code>. If <code>IncludeOpForFullLoad</code> is set to <code>true</code>, the first field of every CDC record is set to I to indicate the INSERT operation at the source. If <code>IncludeOpForFullLoad</code> is set to <code>false</code>, every CDC record is written without a first field to indicate the INSERT operation at the source. For more information about how these settings work together, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps">Indicating Source DB Operations in Migrated S3 Data</a> in the <i>Database Migration Service User Guide.</i>.</p> <note> <p>DMS supports the interaction described preceding between the <code>CdcInsertsOnly</code> and <code>IncludeOpForFullLoad</code> parameters in versions 3.1.4 and later. </p> <p> <code>CdcInsertsOnly</code> and <code>CdcInsertsAndUpdates</code> can't both be set to <code>true</code> for the same endpoint. Set either <code>CdcInsertsOnly</code> or <code>CdcInsertsAndUpdates</code> to <code>true</code> for the same endpoint, but not both.</p> </note>"""
    timestamp_column_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>A value that when nonblank causes DMS to add a column with timestamp information to the endpoint data for an Amazon S3 target.</p> <note> <p>DMS supports the <code>TimestampColumnName</code> parameter in versions 3.1.4 and later.</p> </note> <p>DMS includes an additional <code>STRING</code> column in the .csv or .parquet object files of your migrated data when you set <code>TimestampColumnName</code> to a nonblank value.</p> <p>For a full load, each row of this timestamp column contains a timestamp for when the data was transferred from the source to the target by DMS. </p> <p>For a change data capture (CDC) load, each row of the timestamp column contains the timestamp for the commit of that row in the source database.</p> <p>The string format for this timestamp column value is <code>yyyy-MM-dd HH:mm:ss.SSSSSS</code>. By default, the precision of this value is in microseconds. For a CDC load, the rounding of the precision depends on the commit timestamp supported by DMS for the source database.</p> <p>When the <code>AddColumnName</code> parameter is set to <code>true</code>, DMS also includes a name for the timestamp column that you set with <code>TimestampColumnName</code>.</p>"""
    parquet_timestamp_in_millisecond: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that specifies the precision of any <code>TIMESTAMP</code> column values that are written to an Amazon S3 object file in .parquet format.</p> <note> <p>DMS supports the <code>ParquetTimestampInMillisecond</code> parameter in versions 3.1.4 and later.</p> </note> <p>When <code>ParquetTimestampInMillisecond</code> is set to <code>true</code> or <code>y</code>, DMS writes all <code>TIMESTAMP</code> columns in a .parquet formatted file with millisecond precision. Otherwise, DMS writes them with microsecond precision.</p> <p>Currently, Amazon Athena and Glue can handle only millisecond precision for <code>TIMESTAMP</code> values. Set this parameter to <code>true</code> for S3 endpoint object files that are .parquet formatted only if you plan to query or process the data with Athena or Glue.</p> <note> <p>DMS writes any <code>TIMESTAMP</code> column values written to an S3 file in .csv format with microsecond precision.</p> <p>Setting <code>ParquetTimestampInMillisecond</code> has no effect on the string format of the timestamp column value that is inserted by setting the <code>TimestampColumnName</code> parameter.</p> </note>"""
    cdc_inserts_and_updates: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that enables a change data capture (CDC) load to write INSERT and UPDATE operations to .csv or .parquet (columnar storage) output files. The default setting is <code>false</code>, but when <code>CdcInsertsAndUpdates</code> is set to <code>true</code> or <code>y</code>, only INSERTs and UPDATEs from the source database are migrated to the .csv or .parquet file.</p> <important> <p>DMS supports the use of the .parquet files in versions 3.4.7 and later.</p> </important> <p>How these INSERTs and UPDATEs are recorded depends on the value of the <code>IncludeOpForFullLoad</code> parameter. If <code>IncludeOpForFullLoad</code> is set to <code>true</code>, the first field of every CDC record is set to either <code>I</code> or <code>U</code> to indicate INSERT and UPDATE operations at the source. But if <code>IncludeOpForFullLoad</code> is set to <code>false</code>, CDC records are written without an indication of INSERT or UPDATE operations at the source. For more information about how these settings work together, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps">Indicating Source DB Operations in Migrated S3 Data</a> in the <i>Database Migration Service User Guide.</i>.</p> <note> <p>DMS supports the use of the <code>CdcInsertsAndUpdates</code> parameter in versions 3.3.1 and later.</p> <p> <code>CdcInsertsOnly</code> and <code>CdcInsertsAndUpdates</code> can't both be set to <code>true</code> for the same endpoint. Set either <code>CdcInsertsOnly</code> or <code>CdcInsertsAndUpdates</code> to <code>true</code> for the same endpoint, but not both.</p> </note>"""
    date_partition_enabled: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>When set to <code>true</code>, this parameter partitions S3 bucket folders based on transaction commit dates. The default value is <code>false</code>. For more information about date-based folder partitioning, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.DatePartitioning">Using date-based folder partitioning</a>.</p>"""
    date_partition_sequence: NotRequired[
        "capo_database_migration_service.types.date_partition_sequence_value.DatePartitionSequenceValue"
    ]
    """<p>Identifies the sequence of the date format to use during folder partitioning. The default value is <code>YYYYMMDD</code>. Use this parameter when <code>DatePartitionedEnabled</code> is set to <code>true</code>.</p>"""
    date_partition_delimiter: NotRequired[
        "capo_database_migration_service.types.date_partition_delimiter_value.DatePartitionDelimiterValue"
    ]
    """<p>Specifies a date separating delimiter to use during folder partitioning. The default value is <code>SLASH</code>. Use this parameter when <code>DatePartitionedEnabled</code> is set to <code>true</code>.</p>"""
    use_csv_no_sup_value: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>This setting applies if the S3 output files during a change data capture (CDC) load are written in .csv format. If set to <code>true</code> for columns not included in the supplemental log, DMS uses the value specified by <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-CsvNoSupValue"> <code>CsvNoSupValue</code> </a>. If not set or set to <code>false</code>, DMS uses the null value for these columns.</p> <note> <p>This setting is supported in DMS versions 3.4.1 and later.</p> </note>"""
    csv_no_sup_value: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>This setting only applies if your Amazon S3 output files during a change data capture (CDC) load are written in .csv format. If <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-UseCsvNoSupValue"> <code>UseCsvNoSupValue</code> </a> is set to true, specify a string value that you want DMS to use for all columns not included in the supplemental log. If you do not specify a string value, DMS uses the null value for these columns regardless of the <code>UseCsvNoSupValue</code> setting.</p> <note> <p>This setting is supported in DMS versions 3.4.1 and later.</p> </note>"""
    preserve_transactions: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>If set to <code>true</code>, DMS saves the transaction order for a change data capture (CDC) load on the Amazon S3 target specified by <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-CdcPath"> <code>CdcPath</code> </a>. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.EndpointSettings.CdcPath">Capturing data changes (CDC) including transaction order on the S3 target</a>.</p> <note> <p>This setting is supported in DMS versions 3.4.2 and later.</p> </note>"""
    cdc_path: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Specifies the folder path of CDC files. For an S3 source, this setting is required if a task captures change data; otherwise, it's optional. If <code>CdcPath</code> is set, DMS reads CDC files from this path and replicates the data changes to the target endpoint. For an S3 target if you set <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-PreserveTransactions"> <code>PreserveTransactions</code> </a> to <code>true</code>, DMS verifies that you have set this parameter to a folder path on your S3 target where DMS can save the transaction order for the CDC load. DMS creates this CDC folder path in either your S3 target working directory or the S3 target location specified by <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-BucketFolder"> <code>BucketFolder</code> </a> and <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-BucketName"> <code>BucketName</code> </a>.</p> <p>For example, if you specify <code>CdcPath</code> as <code>MyChangedData</code>, and you specify <code>BucketName</code> as <code>MyTargetBucket</code> but do not specify <code>BucketFolder</code>, DMS creates the CDC folder path following: <code>MyTargetBucket/MyChangedData</code>.</p> <p>If you specify the same <code>CdcPath</code>, and you specify <code>BucketName</code> as <code>MyTargetBucket</code> and <code>BucketFolder</code> as <code>MyTargetData</code>, DMS creates the CDC folder path following: <code>MyTargetBucket/MyTargetData/MyChangedData</code>.</p> <p>For more information on CDC including transaction order on an S3 target, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.EndpointSettings.CdcPath">Capturing data changes (CDC) including transaction order on the S3 target</a>.</p> <note> <p>This setting is supported in DMS versions 3.4.2 and later.</p> </note>"""
    use_task_start_time_for_full_load_timestamp: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>When set to true, this parameter uses the task start time as the timestamp column value instead of the time data is written to target. For full load, when <code>useTaskStartTimeForFullLoadTimestamp</code> is set to <code>true</code>, each row of the timestamp column contains the task start time. For CDC loads, each row of the timestamp column contains the transaction commit time.</p> <p>When <code>useTaskStartTimeForFullLoadTimestamp</code> is set to <code>false</code>, the full load timestamp in the timestamp column increments with the time data arrives at the target. </p>"""
    canned_acl_for_objects: NotRequired[
        "capo_database_migration_service.types.canned_acl_for_objects_value.CannedAclForObjectsValue"
    ]
    """<p>A value that enables DMS to specify a predefined (canned) access control list for objects created in an Amazon S3 bucket as .csv or .parquet files. For more information about Amazon S3 canned ACLs, see <a href="http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl">Canned ACL</a> in the <i>Amazon S3 Developer Guide.</i> </p> <p>The default value is NONE. Valid values include NONE, PRIVATE, PUBLIC_READ, PUBLIC_READ_WRITE, AUTHENTICATED_READ, AWS_EXEC_READ, BUCKET_OWNER_READ, and BUCKET_OWNER_FULL_CONTROL.</p>"""
    add_column_name: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>An optional parameter that, when set to <code>true</code> or <code>y</code>, you can use to add column name information to the .csv output file.</p> <p>The default value is <code>false</code>. Valid values are <code>true</code>, <code>false</code>, <code>y</code>, and <code>n</code>.</p>"""
    cdc_max_batch_interval: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Maximum length of the interval, defined in seconds, after which to output a file to Amazon S3.</p> <p>When <code>CdcMaxBatchInterval</code> and <code>CdcMinFileSize</code> are both specified, the file write is triggered by whichever parameter condition is met first within an DMS CloudFormation template.</p> <p>The default value is 60 seconds.</p>"""
    cdc_min_file_size: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Minimum file size, defined in kilobytes, to reach for a file output to Amazon S3.</p> <p>When <code>CdcMinFileSize</code> and <code>CdcMaxBatchInterval</code> are both specified, the file write is triggered by whichever parameter condition is met first within an DMS CloudFormation template.</p> <p>The default value is 32 MB.</p>"""
    csv_null_value: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>An optional parameter that specifies how DMS treats null values. While handling the null value, you can use this parameter to pass a user-defined string as null when writing to the target. For example, when target columns are nullable, you can use this option to differentiate between the empty string value and the null value. So, if you set this parameter value to the empty string ("" or ''), DMS treats the empty string as the null value instead of <code>NULL</code>.</p> <p>The default value is <code>NULL</code>. Valid values include any valid string.</p>"""
    ignore_header_rows: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>When this value is set to 1, DMS ignores the first row header in a .csv file. A value of 1 turns on the feature; a value of 0 turns off the feature.</p> <p>The default is 0.</p>"""
    max_file_size: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>A value that specifies the maximum size (in KB) of any .csv file to be created while migrating to an S3 target during full load.</p> <p>The default value is 1,048,576 KB (1 GB). Valid values include 1 to 1,048,576.</p>"""
    rfc4180: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>For an S3 source, when this value is set to <code>true</code> or <code>y</code>, each leading double quotation mark has to be followed by an ending double quotation mark. This formatting complies with RFC 4180. When this value is set to <code>false</code> or <code>n</code>, string literals are copied to the target as is. In this case, a delimiter (row or column) signals the end of the field. Thus, you can't use a delimiter as part of the string, because it signals the end of the value.</p> <p>For an S3 target, an optional parameter used to set behavior to comply with RFC 4180 for data migrated to Amazon S3 using .csv file format only. When this value is set to <code>true</code> or <code>y</code> using Amazon S3 as a target, if the data has quotation marks or newline characters in it, DMS encloses the entire column with an additional pair of double quotation marks ("). Every quotation mark within the data is repeated twice.</p> <p>The default value is <code>true</code>. Valid values include <code>true</code>, <code>false</code>, <code>y</code>, and <code>n</code>.</p>"""
    date_partition_timezone: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>When creating an S3 target endpoint, set <code>DatePartitionTimezone</code> to convert the current UTC time into a specified time zone. The conversion occurs when a date partition folder is created and a CDC filename is generated. The time zone format is Area/Location. Use this parameter when <code>DatePartitionedEnabled</code> is set to true, as shown in the following example:</p> <p> <code>s3-settings='{"DatePartitionEnabled": true, "DatePartitionSequence": "YYYYMMDDHH", "DatePartitionDelimiter": "SLASH", "DatePartitionTimezone":"Asia/Seoul", "BucketName": "dms-nattarat-test"}'</code> </p>"""
    add_trailing_padding_character: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Use the S3 target endpoint setting <code>AddTrailingPaddingCharacter</code> to add padding on string data. The default value is <code>false</code>.</p>"""
    expected_bucket_owner: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>To specify a bucket owner and prevent sniping, you can use the <code>ExpectedBucketOwner</code> endpoint setting. </p> <p>Example: <code>--s3-settings='{"ExpectedBucketOwner": "<i>AWS_Account_ID</i>"}'</code> </p> <p>When you make a request to test a connection or perform a migration, S3 checks the account ID of the bucket owner against the specified parameter.</p>"""
    glue_catalog_generation: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>When true, allows Glue to catalog your S3 bucket. Creating an Glue catalog lets you use Athena to query your data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Settings) -> dict:
    out: dict = {}
    if "service_access_role_arn" in value:
        out["ServiceAccessRoleArn"] = value["service_access_role_arn"]
    if "external_table_definition" in value:
        out["ExternalTableDefinition"] = value["external_table_definition"]
    if "csv_row_delimiter" in value:
        out["CsvRowDelimiter"] = value["csv_row_delimiter"]
    if "csv_delimiter" in value:
        out["CsvDelimiter"] = value["csv_delimiter"]
    if "bucket_folder" in value:
        out["BucketFolder"] = value["bucket_folder"]
    if "bucket_name" in value:
        out["BucketName"] = value["bucket_name"]
    if "compression_type" in value:
        import capo_database_migration_service.types.compression_type_value

        out["CompressionType"] = (
            capo_database_migration_service.types.compression_type_value.serialize_aws_json_1_1(
                value["compression_type"]
            )
        )
    if "encryption_mode" in value:
        import capo_database_migration_service.types.encryption_mode_value

        out["EncryptionMode"] = (
            capo_database_migration_service.types.encryption_mode_value.serialize_aws_json_1_1(
                value["encryption_mode"]
            )
        )
    if "server_side_encryption_kms_key_id" in value:
        out["ServerSideEncryptionKmsKeyId"] = value["server_side_encryption_kms_key_id"]
    if "data_format" in value:
        import capo_database_migration_service.types.data_format_value

        out["DataFormat"] = (
            capo_database_migration_service.types.data_format_value.serialize_aws_json_1_1(
                value["data_format"]
            )
        )
    if "encoding_type" in value:
        import capo_database_migration_service.types.encoding_type_value

        out["EncodingType"] = (
            capo_database_migration_service.types.encoding_type_value.serialize_aws_json_1_1(
                value["encoding_type"]
            )
        )
    if "dict_page_size_limit" in value:
        out["DictPageSizeLimit"] = value["dict_page_size_limit"]
    if "row_group_length" in value:
        out["RowGroupLength"] = value["row_group_length"]
    if "data_page_size" in value:
        out["DataPageSize"] = value["data_page_size"]
    if "parquet_version" in value:
        import capo_database_migration_service.types.parquet_version_value

        out["ParquetVersion"] = (
            capo_database_migration_service.types.parquet_version_value.serialize_aws_json_1_1(
                value["parquet_version"]
            )
        )
    if "enable_statistics" in value:
        out["EnableStatistics"] = value["enable_statistics"]
    if "include_op_for_full_load" in value:
        out["IncludeOpForFullLoad"] = value["include_op_for_full_load"]
    if "cdc_inserts_only" in value:
        out["CdcInsertsOnly"] = value["cdc_inserts_only"]
    if "timestamp_column_name" in value:
        out["TimestampColumnName"] = value["timestamp_column_name"]
    if "parquet_timestamp_in_millisecond" in value:
        out["ParquetTimestampInMillisecond"] = value["parquet_timestamp_in_millisecond"]
    if "cdc_inserts_and_updates" in value:
        out["CdcInsertsAndUpdates"] = value["cdc_inserts_and_updates"]
    if "date_partition_enabled" in value:
        out["DatePartitionEnabled"] = value["date_partition_enabled"]
    if "date_partition_sequence" in value:
        import capo_database_migration_service.types.date_partition_sequence_value

        out["DatePartitionSequence"] = (
            capo_database_migration_service.types.date_partition_sequence_value.serialize_aws_json_1_1(
                value["date_partition_sequence"]
            )
        )
    if "date_partition_delimiter" in value:
        import capo_database_migration_service.types.date_partition_delimiter_value

        out["DatePartitionDelimiter"] = (
            capo_database_migration_service.types.date_partition_delimiter_value.serialize_aws_json_1_1(
                value["date_partition_delimiter"]
            )
        )
    if "use_csv_no_sup_value" in value:
        out["UseCsvNoSupValue"] = value["use_csv_no_sup_value"]
    if "csv_no_sup_value" in value:
        out["CsvNoSupValue"] = value["csv_no_sup_value"]
    if "preserve_transactions" in value:
        out["PreserveTransactions"] = value["preserve_transactions"]
    if "cdc_path" in value:
        out["CdcPath"] = value["cdc_path"]
    if "use_task_start_time_for_full_load_timestamp" in value:
        out["UseTaskStartTimeForFullLoadTimestamp"] = value[
            "use_task_start_time_for_full_load_timestamp"
        ]
    if "canned_acl_for_objects" in value:
        import capo_database_migration_service.types.canned_acl_for_objects_value

        out["CannedAclForObjects"] = (
            capo_database_migration_service.types.canned_acl_for_objects_value.serialize_aws_json_1_1(
                value["canned_acl_for_objects"]
            )
        )
    if "add_column_name" in value:
        out["AddColumnName"] = value["add_column_name"]
    if "cdc_max_batch_interval" in value:
        out["CdcMaxBatchInterval"] = value["cdc_max_batch_interval"]
    if "cdc_min_file_size" in value:
        out["CdcMinFileSize"] = value["cdc_min_file_size"]
    if "csv_null_value" in value:
        out["CsvNullValue"] = value["csv_null_value"]
    if "ignore_header_rows" in value:
        out["IgnoreHeaderRows"] = value["ignore_header_rows"]
    if "max_file_size" in value:
        out["MaxFileSize"] = value["max_file_size"]
    if "rfc4180" in value:
        out["Rfc4180"] = value["rfc4180"]
    if "date_partition_timezone" in value:
        out["DatePartitionTimezone"] = value["date_partition_timezone"]
    if "add_trailing_padding_character" in value:
        out["AddTrailingPaddingCharacter"] = value["add_trailing_padding_character"]
    if "expected_bucket_owner" in value:
        out["ExpectedBucketOwner"] = value["expected_bucket_owner"]
    if "glue_catalog_generation" in value:
        out["GlueCatalogGeneration"] = value["glue_catalog_generation"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Settings:
    out: S3Settings = {}  # type: ignore[typeddict-item]
    if data.get("ServiceAccessRoleArn") is not None:
        out["service_access_role_arn"] = data["ServiceAccessRoleArn"]
    if data.get("ExternalTableDefinition") is not None:
        out["external_table_definition"] = data["ExternalTableDefinition"]
    if data.get("CsvRowDelimiter") is not None:
        out["csv_row_delimiter"] = data["CsvRowDelimiter"]
    if data.get("CsvDelimiter") is not None:
        out["csv_delimiter"] = data["CsvDelimiter"]
    if data.get("BucketFolder") is not None:
        out["bucket_folder"] = data["BucketFolder"]
    if data.get("BucketName") is not None:
        out["bucket_name"] = data["BucketName"]
    if data.get("CompressionType") is not None:
        import capo_database_migration_service.types.compression_type_value

        out["compression_type"] = (
            capo_database_migration_service.types.compression_type_value.deserialize_aws_json_1_1(
                data["CompressionType"]
            )
        )
    if data.get("EncryptionMode") is not None:
        import capo_database_migration_service.types.encryption_mode_value

        out["encryption_mode"] = (
            capo_database_migration_service.types.encryption_mode_value.deserialize_aws_json_1_1(
                data["EncryptionMode"]
            )
        )
    if data.get("ServerSideEncryptionKmsKeyId") is not None:
        out["server_side_encryption_kms_key_id"] = data["ServerSideEncryptionKmsKeyId"]
    if data.get("DataFormat") is not None:
        import capo_database_migration_service.types.data_format_value

        out["data_format"] = (
            capo_database_migration_service.types.data_format_value.deserialize_aws_json_1_1(
                data["DataFormat"]
            )
        )
    if data.get("EncodingType") is not None:
        import capo_database_migration_service.types.encoding_type_value

        out["encoding_type"] = (
            capo_database_migration_service.types.encoding_type_value.deserialize_aws_json_1_1(
                data["EncodingType"]
            )
        )
    if data.get("DictPageSizeLimit") is not None:
        out["dict_page_size_limit"] = data["DictPageSizeLimit"]
    if data.get("RowGroupLength") is not None:
        out["row_group_length"] = data["RowGroupLength"]
    if data.get("DataPageSize") is not None:
        out["data_page_size"] = data["DataPageSize"]
    if data.get("ParquetVersion") is not None:
        import capo_database_migration_service.types.parquet_version_value

        out["parquet_version"] = (
            capo_database_migration_service.types.parquet_version_value.deserialize_aws_json_1_1(
                data["ParquetVersion"]
            )
        )
    if data.get("EnableStatistics") is not None:
        out["enable_statistics"] = data["EnableStatistics"]
    if data.get("IncludeOpForFullLoad") is not None:
        out["include_op_for_full_load"] = data["IncludeOpForFullLoad"]
    if data.get("CdcInsertsOnly") is not None:
        out["cdc_inserts_only"] = data["CdcInsertsOnly"]
    if data.get("TimestampColumnName") is not None:
        out["timestamp_column_name"] = data["TimestampColumnName"]
    if data.get("ParquetTimestampInMillisecond") is not None:
        out["parquet_timestamp_in_millisecond"] = data["ParquetTimestampInMillisecond"]
    if data.get("CdcInsertsAndUpdates") is not None:
        out["cdc_inserts_and_updates"] = data["CdcInsertsAndUpdates"]
    if data.get("DatePartitionEnabled") is not None:
        out["date_partition_enabled"] = data["DatePartitionEnabled"]
    if data.get("DatePartitionSequence") is not None:
        import capo_database_migration_service.types.date_partition_sequence_value

        out["date_partition_sequence"] = (
            capo_database_migration_service.types.date_partition_sequence_value.deserialize_aws_json_1_1(
                data["DatePartitionSequence"]
            )
        )
    if data.get("DatePartitionDelimiter") is not None:
        import capo_database_migration_service.types.date_partition_delimiter_value

        out["date_partition_delimiter"] = (
            capo_database_migration_service.types.date_partition_delimiter_value.deserialize_aws_json_1_1(
                data["DatePartitionDelimiter"]
            )
        )
    if data.get("UseCsvNoSupValue") is not None:
        out["use_csv_no_sup_value"] = data["UseCsvNoSupValue"]
    if data.get("CsvNoSupValue") is not None:
        out["csv_no_sup_value"] = data["CsvNoSupValue"]
    if data.get("PreserveTransactions") is not None:
        out["preserve_transactions"] = data["PreserveTransactions"]
    if data.get("CdcPath") is not None:
        out["cdc_path"] = data["CdcPath"]
    if data.get("UseTaskStartTimeForFullLoadTimestamp") is not None:
        out["use_task_start_time_for_full_load_timestamp"] = data[
            "UseTaskStartTimeForFullLoadTimestamp"
        ]
    if data.get("CannedAclForObjects") is not None:
        import capo_database_migration_service.types.canned_acl_for_objects_value

        out["canned_acl_for_objects"] = (
            capo_database_migration_service.types.canned_acl_for_objects_value.deserialize_aws_json_1_1(
                data["CannedAclForObjects"]
            )
        )
    if data.get("AddColumnName") is not None:
        out["add_column_name"] = data["AddColumnName"]
    if data.get("CdcMaxBatchInterval") is not None:
        out["cdc_max_batch_interval"] = data["CdcMaxBatchInterval"]
    if data.get("CdcMinFileSize") is not None:
        out["cdc_min_file_size"] = data["CdcMinFileSize"]
    if data.get("CsvNullValue") is not None:
        out["csv_null_value"] = data["CsvNullValue"]
    if data.get("IgnoreHeaderRows") is not None:
        out["ignore_header_rows"] = data["IgnoreHeaderRows"]
    if data.get("MaxFileSize") is not None:
        out["max_file_size"] = data["MaxFileSize"]
    if data.get("Rfc4180") is not None:
        out["rfc4180"] = data["Rfc4180"]
    if data.get("DatePartitionTimezone") is not None:
        out["date_partition_timezone"] = data["DatePartitionTimezone"]
    if data.get("AddTrailingPaddingCharacter") is not None:
        out["add_trailing_padding_character"] = data["AddTrailingPaddingCharacter"]
    if data.get("ExpectedBucketOwner") is not None:
        out["expected_bucket_owner"] = data["ExpectedBucketOwner"]
    if data.get("GlueCatalogGeneration") is not None:
        out["glue_catalog_generation"] = data["GlueCatalogGeneration"]
    return out
