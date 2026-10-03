"""Generated from Smithy shape ``com.amazonaws.ssmsap#Component``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_ssm_sap.types.application_id
    import capo_ssm_sap.types.associated_host
    import capo_ssm_sap.types.component_id
    import capo_ssm_sap.types.component_id_list
    import capo_ssm_sap.types.component_status
    import capo_ssm_sap.types.component_type
    import capo_ssm_sap.types.database_connection
    import capo_ssm_sap.types.database_id_list
    import capo_ssm_sap.types.host_list
    import capo_ssm_sap.types.resilience
    import capo_ssm_sap.types.sap_instance_number
    import capo_ssm_sap.types.sid
    import capo_ssm_sap.types.ssm_sap_arn


class Component(TypedDict, closed=True):
    component_id: NotRequired["capo_ssm_sap.types.component_id.ComponentId"]
    """<p>The ID of the component.</p>"""
    sid: NotRequired["capo_ssm_sap.types.sid.SID"]
    """<p>The SAP System Identifier of the application component.</p>"""
    system_number: NotRequired[
        "capo_ssm_sap.types.sap_instance_number.SAPInstanceNumber"
    ]
    """<p>The SAP system number of the application component.</p>"""
    parent_component: NotRequired["capo_ssm_sap.types.component_id.ComponentId"]
    """<p>The parent component of a highly available environment. For example, in a highly available SAP on AWS workload, the parent component consists of the entire setup, including the child components.</p>"""
    child_components: NotRequired[
        "capo_ssm_sap.types.component_id_list.ComponentIdList"
    ]
    """<p>The child components of a highly available environment. For example, in a highly available SAP on AWS workload, the child component consists of the primary and secondar instances.</p>"""
    application_id: NotRequired["capo_ssm_sap.types.application_id.ApplicationId"]
    """<p>The ID of the application.</p>"""
    component_type: NotRequired["capo_ssm_sap.types.component_type.ComponentType"]
    """<p>The type of the component.</p>"""
    status: NotRequired["capo_ssm_sap.types.component_status.ComponentStatus"]
    """<p>The status of the component.</p> <ul> <li> <p>ACTIVATED - this status has been deprecated.</p> </li> <li> <p>STARTING - the component is in the process of being started.</p> </li> <li> <p>STOPPED - the component is not running.</p> </li> <li> <p>STOPPING - the component is in the process of being stopped.</p> </li> <li> <p>RUNNING - the component is running.</p> </li> <li> <p>RUNNING_WITH_ERROR - one or more child component(s) of the parent component is not running. Call <a href="https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_GetComponent.html"> <code>GetComponent</code> </a> to review the status of each child component.</p> </li> <li> <p>UNDEFINED - AWS Systems Manager for SAP cannot provide the component status based on the discovered information. Verify your SAP application.</p> </li> </ul>"""
    sap_hostname: NotRequired["str"]
    """<p>The hostname of the component.</p>"""
    sap_feature: NotRequired["str"]
    """<p>The SAP feature of the component.</p>"""
    sap_kernel_version: NotRequired["str"]
    """<p>The kernel version of the component.</p>"""
    hdb_version: NotRequired["str"]
    """<p>The SAP HANA version of the component.</p>"""
    resilience: NotRequired["capo_ssm_sap.types.resilience.Resilience"]
    """<p>Details of the SAP HANA system replication for the component.</p>"""
    associated_host: NotRequired["capo_ssm_sap.types.associated_host.AssociatedHost"]
    """<p>The associated host of the component.</p>"""
    databases: NotRequired["capo_ssm_sap.types.database_id_list.DatabaseIdList"]
    """<p>The SAP HANA databases of the component.</p>"""
    hosts: NotRequired["capo_ssm_sap.types.host_list.HostList"]
    """<p>The hosts of the component.</p>"""
    primary_host: NotRequired["str"]
    """<p>The primary host of the component.</p>"""
    database_connection: NotRequired[
        "capo_ssm_sap.types.database_connection.DatabaseConnection"
    ]
    """<p>The connection specifications for the database of the component.</p>"""
    last_updated: NotRequired["datetime.datetime"]
    """<p>The time at which the component was last updated.</p>"""
    arn: NotRequired["capo_ssm_sap.types.ssm_sap_arn.SsmSapArn"]
    """<p>The Amazon Resource Name (ARN) of the component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Component) -> dict:
    out: dict = {}
    if "component_id" in value:
        out["ComponentId"] = value["component_id"]
    if "sid" in value:
        out["Sid"] = value["sid"]
    if "system_number" in value:
        out["SystemNumber"] = value["system_number"]
    if "parent_component" in value:
        out["ParentComponent"] = value["parent_component"]
    if "child_components" in value:
        import capo_ssm_sap.types.component_id_list

        out["ChildComponents"] = capo_ssm_sap.types.component_id_list.serialize_json(
            value["child_components"]
        )
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "component_type" in value:
        import capo_ssm_sap.types.component_type

        out["ComponentType"] = capo_ssm_sap.types.component_type.serialize_json(
            value["component_type"]
        )
    if "status" in value:
        import capo_ssm_sap.types.component_status

        out["Status"] = capo_ssm_sap.types.component_status.serialize_json(
            value["status"]
        )
    if "sap_hostname" in value:
        out["SapHostname"] = value["sap_hostname"]
    if "sap_feature" in value:
        out["SapFeature"] = value["sap_feature"]
    if "sap_kernel_version" in value:
        out["SapKernelVersion"] = value["sap_kernel_version"]
    if "hdb_version" in value:
        out["HdbVersion"] = value["hdb_version"]
    if "resilience" in value:
        import capo_ssm_sap.types.resilience

        out["Resilience"] = capo_ssm_sap.types.resilience.serialize_json(
            value["resilience"]
        )
    if "associated_host" in value:
        import capo_ssm_sap.types.associated_host

        out["AssociatedHost"] = capo_ssm_sap.types.associated_host.serialize_json(
            value["associated_host"]
        )
    if "databases" in value:
        import capo_ssm_sap.types.database_id_list

        out["Databases"] = capo_ssm_sap.types.database_id_list.serialize_json(
            value["databases"]
        )
    if "hosts" in value:
        import capo_ssm_sap.types.host_list

        out["Hosts"] = capo_ssm_sap.types.host_list.serialize_json(value["hosts"])
    if "primary_host" in value:
        out["PrimaryHost"] = value["primary_host"]
    if "database_connection" in value:
        import capo_ssm_sap.types.database_connection

        out["DatabaseConnection"] = (
            capo_ssm_sap.types.database_connection.serialize_json(
                value["database_connection"]
            )
        )
    if "last_updated" in value:
        import capo_ssm_sap.types._prelude.timestamp

        out["LastUpdated"] = capo_ssm_sap.types._prelude.timestamp.serialize_json(
            value["last_updated"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> Component:
    out: Component = {}  # type: ignore[typeddict-item]
    if data.get("ComponentId") is not None:
        out["component_id"] = data["ComponentId"]
    if data.get("Sid") is not None:
        out["sid"] = data["Sid"]
    if data.get("SystemNumber") is not None:
        out["system_number"] = data["SystemNumber"]
    if data.get("ParentComponent") is not None:
        out["parent_component"] = data["ParentComponent"]
    if data.get("ChildComponents") is not None:
        import capo_ssm_sap.types.component_id_list

        out["child_components"] = capo_ssm_sap.types.component_id_list.deserialize_json(
            data["ChildComponents"]
        )
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("ComponentType") is not None:
        import capo_ssm_sap.types.component_type

        out["component_type"] = capo_ssm_sap.types.component_type.deserialize_json(
            data["ComponentType"]
        )
    if data.get("Status") is not None:
        import capo_ssm_sap.types.component_status

        out["status"] = capo_ssm_sap.types.component_status.deserialize_json(
            data["Status"]
        )
    if data.get("SapHostname") is not None:
        out["sap_hostname"] = data["SapHostname"]
    if data.get("SapFeature") is not None:
        out["sap_feature"] = data["SapFeature"]
    if data.get("SapKernelVersion") is not None:
        out["sap_kernel_version"] = data["SapKernelVersion"]
    if data.get("HdbVersion") is not None:
        out["hdb_version"] = data["HdbVersion"]
    if data.get("Resilience") is not None:
        import capo_ssm_sap.types.resilience

        out["resilience"] = capo_ssm_sap.types.resilience.deserialize_json(
            data["Resilience"]
        )
    if data.get("AssociatedHost") is not None:
        import capo_ssm_sap.types.associated_host

        out["associated_host"] = capo_ssm_sap.types.associated_host.deserialize_json(
            data["AssociatedHost"]
        )
    if data.get("Databases") is not None:
        import capo_ssm_sap.types.database_id_list

        out["databases"] = capo_ssm_sap.types.database_id_list.deserialize_json(
            data["Databases"]
        )
    if data.get("Hosts") is not None:
        import capo_ssm_sap.types.host_list

        out["hosts"] = capo_ssm_sap.types.host_list.deserialize_json(data["Hosts"])
    if data.get("PrimaryHost") is not None:
        out["primary_host"] = data["PrimaryHost"]
    if data.get("DatabaseConnection") is not None:
        import capo_ssm_sap.types.database_connection

        out["database_connection"] = (
            capo_ssm_sap.types.database_connection.deserialize_json(
                data["DatabaseConnection"]
            )
        )
    if data.get("LastUpdated") is not None:
        import capo_ssm_sap.types._prelude.timestamp

        out["last_updated"] = capo_ssm_sap.types._prelude.timestamp.deserialize_json(
            data["LastUpdated"]
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out
