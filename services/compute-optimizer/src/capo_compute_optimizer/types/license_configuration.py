"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.instance_type
    import capo_compute_optimizer.types.license_edition
    import capo_compute_optimizer.types.license_model
    import capo_compute_optimizer.types.license_name
    import capo_compute_optimizer.types.license_version
    import capo_compute_optimizer.types.metrics_source
    import capo_compute_optimizer.types.number_of_cores
    import capo_compute_optimizer.types.operating_system


class LicenseConfiguration(TypedDict, closed=True):
    number_of_cores: "capo_compute_optimizer.types.number_of_cores.NumberOfCores"
    """<p> The current number of cores associated with the instance. </p>"""
    instance_type: NotRequired[
        "capo_compute_optimizer.types.instance_type.InstanceType"
    ]
    """<p> The instance type used in the license. </p>"""
    operating_system: NotRequired[
        "capo_compute_optimizer.types.operating_system.OperatingSystem"
    ]
    """<p> The operating system of the instance. </p>"""
    license_edition: NotRequired[
        "capo_compute_optimizer.types.license_edition.LicenseEdition"
    ]
    """<p> The edition of the license for the application that runs on the instance. </p>"""
    license_name: NotRequired["capo_compute_optimizer.types.license_name.LicenseName"]
    """<p> The name of the license for the application that runs on the instance. </p>"""
    license_model: NotRequired[
        "capo_compute_optimizer.types.license_model.LicenseModel"
    ]
    """<p> The license type associated with the instance. </p>"""
    license_version: NotRequired[
        "capo_compute_optimizer.types.license_version.LicenseVersion"
    ]
    """<p> The version of the license for the application that runs on the instance. </p>"""
    metrics_source: NotRequired[
        "capo_compute_optimizer.types.metrics_source.MetricsSource"
    ]
    """<p> The list of metric sources required to generate recommendations for commercial software licenses. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseConfiguration) -> dict:
    out: dict = {}
    out["numberOfCores"] = value.get("number_of_cores", 0)
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "operating_system" in value:
        out["operatingSystem"] = value["operating_system"]
    if "license_edition" in value:
        import capo_compute_optimizer.types.license_edition

        out["licenseEdition"] = (
            capo_compute_optimizer.types.license_edition.serialize_aws_json_1_0(
                value["license_edition"]
            )
        )
    if "license_name" in value:
        import capo_compute_optimizer.types.license_name

        out["licenseName"] = (
            capo_compute_optimizer.types.license_name.serialize_aws_json_1_0(
                value["license_name"]
            )
        )
    if "license_model" in value:
        import capo_compute_optimizer.types.license_model

        out["licenseModel"] = (
            capo_compute_optimizer.types.license_model.serialize_aws_json_1_0(
                value["license_model"]
            )
        )
    if "license_version" in value:
        out["licenseVersion"] = value["license_version"]
    if "metrics_source" in value:
        import capo_compute_optimizer.types.metrics_source

        out["metricsSource"] = (
            capo_compute_optimizer.types.metrics_source.serialize_aws_json_1_0(
                value["metrics_source"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LicenseConfiguration:
    out: LicenseConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("numberOfCores") is not None:
        out["number_of_cores"] = data["numberOfCores"]
    else:
        out["number_of_cores"] = 0
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    if data.get("operatingSystem") is not None:
        out["operating_system"] = data["operatingSystem"]
    if data.get("licenseEdition") is not None:
        import capo_compute_optimizer.types.license_edition

        out["license_edition"] = (
            capo_compute_optimizer.types.license_edition.deserialize_aws_json_1_0(
                data["licenseEdition"]
            )
        )
    if data.get("licenseName") is not None:
        import capo_compute_optimizer.types.license_name

        out["license_name"] = (
            capo_compute_optimizer.types.license_name.deserialize_aws_json_1_0(
                data["licenseName"]
            )
        )
    if data.get("licenseModel") is not None:
        import capo_compute_optimizer.types.license_model

        out["license_model"] = (
            capo_compute_optimizer.types.license_model.deserialize_aws_json_1_0(
                data["licenseModel"]
            )
        )
    if data.get("licenseVersion") is not None:
        out["license_version"] = data["licenseVersion"]
    if data.get("metricsSource") is not None:
        import capo_compute_optimizer.types.metrics_source

        out["metrics_source"] = (
            capo_compute_optimizer.types.metrics_source.deserialize_aws_json_1_0(
                data["metricsSource"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LicenseConfiguration) -> dict:
    out: dict = {}
    out["numberOfCores"] = value.get("number_of_cores", 0)
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "operating_system" in value:
        out["operatingSystem"] = value["operating_system"]
    if "license_edition" in value:
        import capo_compute_optimizer.types.license_edition

        out["licenseEdition"] = (
            capo_compute_optimizer.types.license_edition.serialize_cbor(
                value["license_edition"]
            )
        )
    if "license_name" in value:
        import capo_compute_optimizer.types.license_name

        out["licenseName"] = capo_compute_optimizer.types.license_name.serialize_cbor(
            value["license_name"]
        )
    if "license_model" in value:
        import capo_compute_optimizer.types.license_model

        out["licenseModel"] = capo_compute_optimizer.types.license_model.serialize_cbor(
            value["license_model"]
        )
    if "license_version" in value:
        out["licenseVersion"] = value["license_version"]
    if "metrics_source" in value:
        import capo_compute_optimizer.types.metrics_source

        out["metricsSource"] = (
            capo_compute_optimizer.types.metrics_source.serialize_cbor(
                value["metrics_source"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> LicenseConfiguration:
    out: LicenseConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("numberOfCores") is not None:
        out["number_of_cores"] = data["numberOfCores"]
    else:
        out["number_of_cores"] = 0
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    if data.get("operatingSystem") is not None:
        out["operating_system"] = data["operatingSystem"]
    if data.get("licenseEdition") is not None:
        import capo_compute_optimizer.types.license_edition

        out["license_edition"] = (
            capo_compute_optimizer.types.license_edition.deserialize_cbor(
                data["licenseEdition"]
            )
        )
    if data.get("licenseName") is not None:
        import capo_compute_optimizer.types.license_name

        out["license_name"] = (
            capo_compute_optimizer.types.license_name.deserialize_cbor(
                data["licenseName"]
            )
        )
    if data.get("licenseModel") is not None:
        import capo_compute_optimizer.types.license_model

        out["license_model"] = (
            capo_compute_optimizer.types.license_model.deserialize_cbor(
                data["licenseModel"]
            )
        )
    if data.get("licenseVersion") is not None:
        out["license_version"] = data["licenseVersion"]
    if data.get("metricsSource") is not None:
        import capo_compute_optimizer.types.metrics_source

        out["metrics_source"] = (
            capo_compute_optimizer.types.metrics_source.deserialize_cbor(
                data["metricsSource"]
            )
        )
    return out
