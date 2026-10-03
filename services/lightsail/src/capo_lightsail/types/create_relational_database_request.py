"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateRelationalDatabaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.sensitive_string
    import capo_lightsail.types.string
    import capo_lightsail.types.tag_list


class CreateRelationalDatabaseRequest(TypedDict, closed=True):
    relational_database_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name to use for your new Lightsail database resource.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 2 to 255 alphanumeric characters, or hyphens.</p> </li> <li> <p>The first and last character must be a letter or number.</p> </li> </ul>"""
    availability_zone: NotRequired["capo_lightsail.types.string.string"]
    """<p>The Availability Zone in which to create your new database. Use the <code>us-east-2a</code> case-sensitive format.</p> <p>You can get a list of Availability Zones by using the <code>get regions</code> operation. Be sure to add the <code>include relational database Availability Zones</code> parameter to your request.</p>"""
    relational_database_blueprint_id: "capo_lightsail.types.string.string"
    """<p>The blueprint ID for your new database. A blueprint describes the major engine version of a database.</p> <p>You can get a list of database blueprints IDs by using the <code>get relational database blueprints</code> operation.</p>"""
    relational_database_bundle_id: "capo_lightsail.types.string.string"
    """<p>The bundle ID for your new database. A bundle describes the performance specifications for your database.</p> <p>You can get a list of database bundle IDs by using the <code>get relational database bundles</code> operation.</p>"""
    master_database_name: "capo_lightsail.types.string.string"
    """<p>The meaning of this parameter differs according to the database engine you use.</p> <p> <b>MySQL</b> </p> <p>The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, no database is created in the database resource.</p> <p>Constraints:</p> <ul> <li> <p>Must contain 1 to 64 letters or numbers.</p> </li> <li> <p>Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0- 9).</p> </li> <li> <p>Can't be a word reserved by the specified database engine.</p> <p>For more information about reserved words in MySQL, see the Keywords and Reserved Words articles for <a href="https://dev.mysql.com/doc/refman/5.6/en/keywords.html">MySQL 5.6</a>, <a href="https://dev.mysql.com/doc/refman/5.7/en/keywords.html">MySQL 5.7</a>, and <a href="https://dev.mysql.com/doc/refman/8.0/en/keywords.html">MySQL 8.0</a>.</p> </li> </ul> <p> <b>PostgreSQL</b> </p> <p>The name of the database to create when the Lightsail database resource is created. If this parameter isn't specified, a database named <code>postgres</code> is created in the database resource.</p> <p>Constraints:</p> <ul> <li> <p>Must contain 1 to 63 letters or numbers.</p> </li> <li> <p>Must begin with a letter. Subsequent characters can be letters, underscores, or digits (0- 9).</p> </li> <li> <p>Can't be a word reserved by the specified database engine.</p> <p>For more information about reserved words in PostgreSQL, see the SQL Key Words articles for <a href="https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html">PostgreSQL 9.6</a>, <a href="https://www.postgresql.org/docs/10/sql-keywords-appendix.html">PostgreSQL 10</a>, <a href="https://www.postgresql.org/docs/11/sql-keywords-appendix.html">PostgreSQL 11</a>, and <a href="https://www.postgresql.org/docs/12/sql-keywords-appendix.html">PostgreSQL 12</a>.</p> </li> </ul>"""
    master_username: "capo_lightsail.types.string.string"
    """<p>The name for the master user.</p> <p> <b>MySQL</b> </p> <p>Constraints:</p> <ul> <li> <p>Required for MySQL.</p> </li> <li> <p>Must be 1 to 16 letters or numbers. Can contain underscores.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't be a reserved word for the chosen database engine.</p> <p>For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for <a href="https://dev.mysql.com/doc/refman/5.6/en/keywords.html">MySQL 5.6</a>, <a href="https://dev.mysql.com/doc/refman/5.7/en/keywords.html">MySQL 5.7</a>, or <a href="https://dev.mysql.com/doc/refman/8.0/en/keywords.html">MySQL 8.0</a>.</p> </li> </ul> <p> <b>PostgreSQL</b> </p> <p>Constraints:</p> <ul> <li> <p>Required for PostgreSQL.</p> </li> <li> <p>Must be 1 to 63 letters or numbers. Can contain underscores.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't be a reserved word for the chosen database engine.</p> <p>For more information about reserved words in MySQL 5.6 or 5.7, see the Keywords and Reserved Words articles for <a href="https://www.postgresql.org/docs/9.6/sql-keywords-appendix.html">PostgreSQL 9.6</a>, <a href="https://www.postgresql.org/docs/10/sql-keywords-appendix.html">PostgreSQL 10</a>, <a href="https://www.postgresql.org/docs/11/sql-keywords-appendix.html">PostgreSQL 11</a>, and <a href="https://www.postgresql.org/docs/12/sql-keywords-appendix.html">PostgreSQL 12</a>.</p> </li> </ul>"""
    master_user_password: NotRequired[
        "capo_lightsail.types.sensitive_string.SensitiveString"
    ]
    """<p>The password for the master user. The password can include any printable ASCII character except \"/\", \"\"\", or \"@\". It cannot contain spaces.</p> <p> <b>MySQL</b> </p> <p>Constraints: Must contain from 8 to 41 characters.</p> <p> <b>PostgreSQL</b> </p> <p>Constraints: Must contain from 8 to 128 characters.</p>"""
    preferred_backup_window: NotRequired["capo_lightsail.types.string.string"]
    """<p>The daily time range during which automated backups are created for your new database if automated backups are enabled.</p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. For more information about the preferred backup window time blocks for each region, see the <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html#USER_WorkingWithAutomatedBackups.BackupWindow">Working With Backups</a> guide in the Amazon Relational Database Service documentation.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the <code>hh24:mi-hh24:mi</code> format.</p> <p>Example: <code>16:00-16:30</code> </p> </li> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Must not conflict with the preferred maintenance window.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> </ul>"""
    preferred_maintenance_window: NotRequired["capo_lightsail.types.string.string"]
    """<p>The weekly time range during which system maintenance can occur on your new database.</p> <p>The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.</p> <p>Constraints:</p> <ul> <li> <p>Must be in the <code>ddd:hh24:mi-ddd:hh24:mi</code> format.</p> </li> <li> <p>Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun.</p> </li> <li> <p>Must be at least 30 minutes.</p> </li> <li> <p>Specified in Coordinated Universal Time (UTC).</p> </li> <li> <p>Example: <code>Tue:17:00-Tue:17:30</code> </p> </li> </ul>"""
    publicly_accessible: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Specifies the accessibility options for your new database. A value of <code>true</code> specifies a database that is available to resources outside of your Lightsail account. A value of <code>false</code> specifies a database that is available only to your Lightsail resources in the same region as your database.</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRelationalDatabaseRequest) -> dict:
    out: dict = {}
    out["relationalDatabaseName"] = value["relational_database_name"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    out["relationalDatabaseBlueprintId"] = value["relational_database_blueprint_id"]
    out["relationalDatabaseBundleId"] = value["relational_database_bundle_id"]
    out["masterDatabaseName"] = value["master_database_name"]
    out["masterUsername"] = value["master_username"]
    if "master_user_password" in value:
        out["masterUserPassword"] = value["master_user_password"]
    if "preferred_backup_window" in value:
        out["preferredBackupWindow"] = value["preferred_backup_window"]
    if "preferred_maintenance_window" in value:
        out["preferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "publicly_accessible" in value:
        out["publiclyAccessible"] = value["publicly_accessible"]
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRelationalDatabaseRequest:
    out: CreateRelationalDatabaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("relationalDatabaseName") is not None:
        out["relational_database_name"] = data["relationalDatabaseName"]
    else:
        raise DeserializationError(
            "CreateRelationalDatabaseRequest.relational_database_name required"
        )
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("relationalDatabaseBlueprintId") is not None:
        out["relational_database_blueprint_id"] = data["relationalDatabaseBlueprintId"]
    else:
        raise DeserializationError(
            "CreateRelationalDatabaseRequest.relational_database_blueprint_id required"
        )
    if data.get("relationalDatabaseBundleId") is not None:
        out["relational_database_bundle_id"] = data["relationalDatabaseBundleId"]
    else:
        raise DeserializationError(
            "CreateRelationalDatabaseRequest.relational_database_bundle_id required"
        )
    if data.get("masterDatabaseName") is not None:
        out["master_database_name"] = data["masterDatabaseName"]
    else:
        raise DeserializationError(
            "CreateRelationalDatabaseRequest.master_database_name required"
        )
    if data.get("masterUsername") is not None:
        out["master_username"] = data["masterUsername"]
    else:
        raise DeserializationError(
            "CreateRelationalDatabaseRequest.master_username required"
        )
    if data.get("masterUserPassword") is not None:
        out["master_user_password"] = data["masterUserPassword"]
    if data.get("preferredBackupWindow") is not None:
        out["preferred_backup_window"] = data["preferredBackupWindow"]
    if data.get("preferredMaintenanceWindow") is not None:
        out["preferred_maintenance_window"] = data["preferredMaintenanceWindow"]
    if data.get("publiclyAccessible") is not None:
        out["publicly_accessible"] = data["publiclyAccessible"]
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
