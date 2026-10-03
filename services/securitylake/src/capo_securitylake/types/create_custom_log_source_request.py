"""Generated from Smithy shape ``com.amazonaws.securitylake#CreateCustomLogSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securitylake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securitylake.types.custom_log_source_configuration
    import capo_securitylake.types.custom_log_source_name
    import capo_securitylake.types.custom_log_source_version
    import capo_securitylake.types.ocsf_event_class_list


class CreateCustomLogSourceRequest(TypedDict, closed=True):
    source_name: "capo_securitylake.types.custom_log_source_name.CustomLogSourceName"
    """<p>Specify the name for a third-party custom source. This must be a Regionally unique value. The <code>sourceName</code> you enter here, is used in the <code>LogProviderRole</code> name which follows the convention <code>AmazonSecurityLake-Provider-{name of the custom source}-{region}</code>. You must use a <code>CustomLogSource</code> name that is shorter than or equal to 20 characters. This ensures that the <code>LogProviderRole</code> name is below the 64 character limit.</p>"""
    source_version: NotRequired[
        "capo_securitylake.types.custom_log_source_version.CustomLogSourceVersion"
    ]
    """<p>Specify the source version for the third-party custom source, to limit log collection to a specific version of custom data source.</p>"""
    event_classes: NotRequired[
        "capo_securitylake.types.ocsf_event_class_list.OcsfEventClassList"
    ]
    """<p>The Open Cybersecurity Schema Framework (OCSF) event classes which describes the type of data that the custom source will send to Security Lake. For the list of supported event classes, see the <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/adding-custom-sources.html#ocsf-eventclass">Amazon Security Lake User Guide</a>.</p>"""
    configuration: "capo_securitylake.types.custom_log_source_configuration.CustomLogSourceConfiguration"
    """<p>The configuration used for the third-party custom source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCustomLogSourceRequest) -> dict:
    out: dict = {}
    out["sourceName"] = value["source_name"]
    if "source_version" in value:
        out["sourceVersion"] = value["source_version"]
    if "event_classes" in value:
        import capo_securitylake.types.ocsf_event_class_list

        out["eventClasses"] = (
            capo_securitylake.types.ocsf_event_class_list.serialize_json(
                value["event_classes"]
            )
        )
    import capo_securitylake.types.custom_log_source_configuration

    out["configuration"] = (
        capo_securitylake.types.custom_log_source_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateCustomLogSourceRequest:
    out: CreateCustomLogSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceName") is not None:
        out["source_name"] = data["sourceName"]
    else:
        raise DeserializationError("CreateCustomLogSourceRequest.source_name required")
    if data.get("sourceVersion") is not None:
        out["source_version"] = data["sourceVersion"]
    if data.get("eventClasses") is not None:
        import capo_securitylake.types.ocsf_event_class_list

        out["event_classes"] = (
            capo_securitylake.types.ocsf_event_class_list.deserialize_json(
                data["eventClasses"]
            )
        )
    if data.get("configuration") is not None:
        import capo_securitylake.types.custom_log_source_configuration

        out["configuration"] = (
            capo_securitylake.types.custom_log_source_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCustomLogSourceRequest.configuration required"
        )
    return out
