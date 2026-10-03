"""Generated from Smithy shape ``com.amazonaws.ecs#ContainerDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.container_dependencies
    import capo_ecs.types.container_restart_policy
    import capo_ecs.types.docker_labels_map
    import capo_ecs.types.environment_files
    import capo_ecs.types.environment_variables
    import capo_ecs.types.firelens_configuration
    import capo_ecs.types.health_check
    import capo_ecs.types.host_entry_list
    import capo_ecs.types.integer
    import capo_ecs.types.linux_parameters
    import capo_ecs.types.log_configuration
    import capo_ecs.types.mount_point_list
    import capo_ecs.types.port_mapping_list
    import capo_ecs.types.repository_credentials
    import capo_ecs.types.resource_requirements
    import capo_ecs.types.secret_list
    import capo_ecs.types.string
    import capo_ecs.types.string_list
    import capo_ecs.types.system_controls
    import capo_ecs.types.ulimit_list
    import capo_ecs.types.version_consistency
    import capo_ecs.types.volume_from_list


class ContainerDefinition(TypedDict, closed=True):
    name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of a container. If you're linking multiple containers together in a task definition, the <code>name</code> of one container can be entered in the <code>links</code> of another container to connect the containers. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. This parameter maps to <code>name</code> in the docker container create command and the <code>--name</code> option to docker run. </p>"""
    image: NotRequired["capo_ecs.types.string.String"]
    """<p>The image used to start a container. This string is passed directly to the Docker daemon. By default, images in the Docker Hub registry are available. Other repositories are specified with either <code> <i>repository-url</i>/<i>image</i>:<i>tag</i> </code> or <code> <i>repository-url</i>/<i>image</i>@<i>digest</i> </code>. For images using tags (repository-url/image:tag), up to 255 characters total are allowed, including letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs (#). For images using digests (repository-url/image@digest), the 255 character limit applies only to the repository URL and image name (everything before the @ sign). The only supported hash function is sha256, and the hash value after sha256: must be exactly 64 characters (only letters A-F, a-f, and numbers 0-9 are allowed). This parameter maps to <code>Image</code> in the docker container create command and the <code>IMAGE</code> parameter of docker run.</p> <ul> <li> <p>When a new task starts, the Amazon ECS container agent pulls the latest version of the specified image and tag for the container to use. However, subsequent updates to a repository image aren't propagated to already running tasks.</p> </li> <li> <p>Images in Amazon ECR repositories can be specified by either using the full <code>registry/repository:tag</code> or <code>registry/repository@digest</code>. For example, <code>012345678910.dkr.ecr.&lt;region-name&gt;.amazonaws.com/&lt;repository-name&gt;:latest</code> or <code>012345678910.dkr.ecr.&lt;region-name&gt;.amazonaws.com/&lt;repository-name&gt;@sha256:94afd1f2e64d908bc90dbca0035a5b567EXAMPLE</code>. </p> </li> <li> <p>Images in official repositories on Docker Hub use a single name (for example, <code>ubuntu</code> or <code>mongo</code>).</p> </li> <li> <p>Images in other repositories on Docker Hub are qualified with an organization name (for example, <code>amazon/amazon-ecs-agent</code>).</p> </li> <li> <p>Images in other online repositories are qualified further by a domain name (for example, <code>quay.io/assemblyline/ubuntu</code>).</p> </li> </ul>"""
    repository_credentials: NotRequired[
        "capo_ecs.types.repository_credentials.RepositoryCredentials"
    ]
    """<p>The private repository authentication credentials to use.</p>"""
    cpu: "capo_ecs.types.integer.Integer"
    """<p>The number of <code>cpu</code> units reserved for the container. This parameter maps to <code>CpuShares</code> in the docker container create command and the <code>--cpu-shares</code> option to docker run.</p> <p>This field is optional for tasks using the Fargate launch type, and the only requirement is that the total amount of CPU reserved for all containers within a task be lower than the task-level <code>cpu</code> value.</p> <note> <p>You can determine the number of CPU units that are available per EC2 instance type by multiplying the vCPUs listed for that instance type on the <a href="http://aws.amazon.com/ec2/instance-types/">Amazon EC2 Instances</a> detail page by 1,024.</p> </note> <p>Linux containers share unallocated CPU units with other containers on the container instance with the same ratio as their allocated amount. For example, if you run a single-container task on a single-core instance type with 512 CPU units specified for that container, and that's the only task running on the container instance, that container could use the full 1,024 CPU unit share at any given time. However, if you launched another copy of the same task on that container instance, each task is guaranteed a minimum of 512 CPU units when needed. Moreover, each container could float to higher CPU usage if the other container was not using it. If both tasks were 100% active all of the time, they would be limited to 512 CPU units.</p> <p>On Linux container instances, the Docker daemon on the container instance uses the CPU value to calculate the relative CPU share ratios for running containers. The minimum valid CPU share value that the Linux kernel allows is 2, and the maximum valid CPU share value that the Linux kernel allows is 262144. However, the CPU parameter isn't required, and you can use CPU values below 2 or above 262144 in your container definitions. For CPU values below 2 (including null) or above 262144, the behavior varies based on your Amazon ECS container agent version:</p> <ul> <li> <p> <b>Agent versions less than or equal to 1.1.0:</b> Null and zero CPU values are passed to Docker as 0, which Docker then converts to 1,024 CPU shares. CPU values of 1 are passed to Docker as 1, which the Linux kernel converts to two CPU shares.</p> </li> <li> <p> <b>Agent versions greater than or equal to 1.2.0:</b> Null, zero, and CPU values of 1 are passed to Docker as 2.</p> </li> <li> <p> <b>Agent versions greater than or equal to 1.84.0:</b> CPU values greater than 256 vCPU are passed to Docker as 256, which is equivalent to 262144 CPU shares.</p> </li> </ul> <p>On Windows container instances, the CPU limit is enforced as an absolute limit, or a quota. Windows containers only have access to the specified amount of CPU that's described in the task definition. A null or zero CPU value is passed to Docker as <code>0</code>, which Windows interprets as 1% of one CPU.</p>"""
    memory: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The amount (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. The total amount of memory reserved for all containers within a task must be lower than the task <code>memory</code> value, if one is specified. This parameter maps to <code>Memory</code> in the docker container create command and the <code>--memory</code> option to docker run.</p> <p>If using the Fargate launch type, this parameter is optional.</p> <p>If using the EC2 launch type, you must specify either a task-level memory value or a container-level memory value. If you specify both a container-level <code>memory</code> and <code>memoryReservation</code> value, <code>memory</code> must be greater than <code>memoryReservation</code>. If you specify <code>memoryReservation</code>, then that value is subtracted from the available memory resources for the container instance where the container is placed. Otherwise, the value of <code>memory</code> is used.</p> <p>The Docker 20.10.0 or later daemon reserves a minimum of 6 MiB of memory for a container. So, don't specify less than 6 MiB of memory for your containers. </p> <p>The Docker 19.03.13-ce or earlier daemon reserves a minimum of 4 MiB of memory for a container. So, don't specify less than 4 MiB of memory for your containers.</p>"""
    memory_reservation: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The soft limit (in MiB) of memory to reserve for the container. When system memory is under heavy contention, Docker attempts to keep the container memory to this soft limit. However, your container can consume more memory when it needs to, up to either the hard limit specified with the <code>memory</code> parameter (if applicable), or all of the available memory on the container instance, whichever comes first. This parameter maps to <code>MemoryReservation</code> in the docker container create command and the <code>--memory-reservation</code> option to docker run.</p> <p>If a task-level memory value is not specified, you must specify a non-zero integer for one or both of <code>memory</code> or <code>memoryReservation</code> in a container definition. If you specify both, <code>memory</code> must be greater than <code>memoryReservation</code>. If you specify <code>memoryReservation</code>, then that value is subtracted from the available memory resources for the container instance where the container is placed. Otherwise, the value of <code>memory</code> is used.</p> <p>For example, if your container normally uses 128 MiB of memory, but occasionally bursts to 256 MiB of memory for short periods of time, you can set a <code>memoryReservation</code> of 128 MiB, and a <code>memory</code> hard limit of 300 MiB. This configuration would allow the container to only reserve 128 MiB of memory from the remaining resources on the container instance, but also allow the container to consume more memory resources when needed.</p> <p>The Docker 20.10.0 or later daemon reserves a minimum of 6 MiB of memory for a container. So, don't specify less than 6 MiB of memory for your containers. </p> <p>The Docker 19.03.13-ce or earlier daemon reserves a minimum of 4 MiB of memory for a container. So, don't specify less than 4 MiB of memory for your containers.</p>"""
    links: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The <code>links</code> parameter allows containers to communicate with each other without the need for port mappings. This parameter is only supported if the network mode of a task definition is <code>bridge</code>. The <code>name:internalName</code> construct is analogous to <code>name:alias</code> in Docker links. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed.. This parameter maps to <code>Links</code> in the docker container create command and the <code>--link</code> option to docker run.</p> <note> <p>This parameter is not supported for Windows containers.</p> </note> <important> <p>Containers that are collocated on a single container instance may be able to communicate with each other without requiring links or host port mappings. Network isolation is achieved on the container instance using security groups and VPC settings.</p> </important>"""
    port_mappings: NotRequired["capo_ecs.types.port_mapping_list.PortMappingList"]
    """<p>The list of port mappings for the container. Port mappings allow containers to access ports on the host container instance to send or receive traffic.</p> <p>For task definitions that use the <code>awsvpc</code> network mode, only specify the <code>containerPort</code>. The <code>hostPort</code> can be left blank or it must be the same value as the <code>containerPort</code>.</p> <p>Port mappings on Windows use the <code>NetNAT</code> gateway address rather than <code>localhost</code>. There's no loopback for port mappings on Windows, so you can't access a container's mapped port from the host itself. </p> <p>This parameter maps to <code>PortBindings</code> in the docker container create command and the <code>--publish</code> option to docker run. If the network mode of a task definition is set to <code>none</code>, then you can't specify port mappings. If the network mode of a task definition is set to <code>host</code>, then host ports must either be undefined or they must match the container port in the port mapping.</p> <note> <p>After a task reaches the <code>RUNNING</code> status, manual and automatic host and container port assignments are visible in the <b>Network Bindings</b> section of a container description for a selected task in the Amazon ECS console. The assignments are also visible in the <code>networkBindings</code> section <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html">DescribeTasks</a> responses.</p> </note>"""
    essential: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>If the <code>essential</code> parameter of a container is marked as <code>true</code>, and that container fails or stops for any reason, all other containers that are part of the task are stopped. If the <code>essential</code> parameter of a container is marked as <code>false</code>, its failure doesn't affect the rest of the containers in a task. If this parameter is omitted, a container is assumed to be essential.</p> <p>All tasks must have at least one essential container. If you have an application that's composed of multiple containers, group containers that are used for a common purpose into components, and separate the different components into multiple task definitions. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/application_architecture.html">Application Architecture</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    restart_policy: NotRequired[
        "capo_ecs.types.container_restart_policy.ContainerRestartPolicy"
    ]
    """<p>The restart policy for a container. When you set up a restart policy, Amazon ECS can restart the container without needing to replace the task. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-restart-policy.html">Restart individual containers in Amazon ECS tasks with container restart policies</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    entry_point: NotRequired["capo_ecs.types.string_list.StringList"]
    """<important> <p>Early versions of the Amazon ECS container agent don't properly handle <code>entryPoint</code> parameters. If you have problems using <code>entryPoint</code>, update your container agent or enter your commands and arguments as <code>command</code> array items instead.</p> </important> <p>The entry point that's passed to the container. This parameter maps to <code>Entrypoint</code> in the docker container create command and the <code>--entrypoint</code> option to docker run.</p>"""
    command: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The command that's passed to the container. This parameter maps to <code>Cmd</code> in the docker container create command and the <code>COMMAND</code> parameter to docker run. If there are multiple arguments, each argument is a separated string in the array.</p>"""
    environment: NotRequired[
        "capo_ecs.types.environment_variables.EnvironmentVariables"
    ]
    """<p>The environment variables to pass to a container. This parameter maps to <code>Env</code> in the docker container create command and the <code>--env</code> option to docker run.</p> <important> <p>We don't recommend that you use plaintext environment variables for sensitive information, such as credential data.</p> </important>"""
    environment_files: NotRequired["capo_ecs.types.environment_files.EnvironmentFiles"]
    """<p>A list of files containing the environment variables to pass to a container. This parameter maps to the <code>--env-file</code> option to docker run.</p> <p>You can specify up to ten environment files. The file must have a <code>.env</code> file extension. Each line in an environment file contains an environment variable in <code>VARIABLE=VALUE</code> format. Lines beginning with <code>#</code> are treated as comments and are ignored.</p> <p>If there are environment variables specified using the <code>environment</code> parameter in a container definition, they take precedence over the variables contained within an environment file. If multiple environment files are specified that contain the same variable, they're processed from the top down. We recommend that you use unique variable names. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/taskdef-envfiles.html">Specifying Environment Variables</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    mount_points: NotRequired["capo_ecs.types.mount_point_list.MountPointList"]
    """<p>The mount points for data volumes in your container.</p> <p>This parameter maps to <code>Volumes</code> in the docker container create command and the <code>--volume</code> option to docker run.</p> <p>Windows containers can mount whole directories on the same drive as <code>$env:ProgramData</code>. Windows containers can't mount directories on a different drive, and mount point can't be across drives.</p>"""
    volumes_from: NotRequired["capo_ecs.types.volume_from_list.VolumeFromList"]
    """<p>Data volumes to mount from another container. This parameter maps to <code>VolumesFrom</code> in the docker container create command and the <code>--volumes-from</code> option to docker run.</p>"""
    linux_parameters: NotRequired["capo_ecs.types.linux_parameters.LinuxParameters"]
    """<p>Linux-specific modifications that are applied to the default Docker container configuration, such as Linux kernel capabilities. For more information see <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_KernelCapabilities.html">KernelCapabilities</a>.</p> <note> <p>This parameter is not supported for Windows containers.</p> </note>"""
    secrets: NotRequired["capo_ecs.types.secret_list.SecretList"]
    """<p>The secrets to pass to the container. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specifying-sensitive-data.html">Specifying Sensitive Data</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    depends_on: NotRequired[
        "capo_ecs.types.container_dependencies.ContainerDependencies"
    ]
    """<p>The dependencies defined for container startup and shutdown. A container can contain multiple dependencies on other containers in a task definition. When a dependency is defined for container startup, for container shutdown it is reversed.</p> <p>For tasks using the EC2 launch type, the container instances require at least version 1.26.0 of the container agent to turn on container dependencies. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html">Updating the Amazon ECS Container Agent</a> in the <i>Amazon Elastic Container Service Developer Guide</i>. If you're using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the <code>ecs-init</code> package. If your container instances are launched from version <code>20190301</code> or later, then they contain the required versions of the container agent and <code>ecs-init</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html">Amazon ECS-optimized Linux AMI</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>For tasks using the Fargate launch type, the task or service requires the following platforms:</p> <ul> <li> <p>Linux platform version <code>1.3.0</code> or later.</p> </li> <li> <p>Windows platform version <code>1.0.0</code> or later.</p> </li> </ul>"""
    start_timeout: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>Time duration (in seconds) to wait before giving up on resolving dependencies for a container. For example, you specify two containers in a task definition with containerA having a dependency on containerB reaching a <code>COMPLETE</code>, <code>SUCCESS</code>, or <code>HEALTHY</code> status. If a <code>startTimeout</code> value is specified for containerB and it doesn't reach the desired status within that time then containerA gives up and not start. This results in the task transitioning to a <code>STOPPED</code> state.</p> <note> <p>When the <code>ECS_CONTAINER_START_TIMEOUT</code> container agent configuration variable is used, it's enforced independently from this start timeout value.</p> </note> <p>For tasks using the Fargate launch type, the task or service requires the following platforms:</p> <ul> <li> <p>Linux platform version <code>1.3.0</code> or later.</p> </li> <li> <p>Windows platform version <code>1.0.0</code> or later.</p> </li> </ul> <p>For tasks using the EC2 launch type, your container instances require at least version <code>1.26.0</code> of the container agent to use a container start timeout value. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html">Updating the Amazon ECS Container Agent</a> in the <i>Amazon Elastic Container Service Developer Guide</i>. If you're using an Amazon ECS-optimized Linux AMI, your instance needs at least version <code>1.26.0-1</code> of the <code>ecs-init</code> package. If your container instances are launched from version <code>20190301</code> or later, then they contain the required versions of the container agent and <code>ecs-init</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html">Amazon ECS-optimized Linux AMI</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>The valid values for Fargate are 2-120 seconds.</p>"""
    stop_timeout: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>Time duration (in seconds) to wait before the container is forcefully killed if it doesn't exit normally on its own.</p> <p>For tasks using the Fargate launch type, the task or service requires the following platforms:</p> <ul> <li> <p>Linux platform version <code>1.3.0</code> or later.</p> </li> <li> <p>Windows platform version <code>1.0.0</code> or later.</p> </li> </ul> <p>For tasks that use the Fargate launch type, the max stop timeout value is 120 seconds and if the parameter is not specified, the default value of 30 seconds is used.</p> <p>For tasks that use the EC2 launch type, if the <code>stopTimeout</code> parameter isn't specified, the value set for the Amazon ECS container agent configuration variable <code>ECS_CONTAINER_STOP_TIMEOUT</code> is used. If neither the <code>stopTimeout</code> parameter or the <code>ECS_CONTAINER_STOP_TIMEOUT</code> agent configuration variable are set, then the default values of 30 seconds for Linux containers and 30 seconds on Windows containers are used. Your container instances require at least version 1.26.0 of the container agent to use a container stop timeout value. However, we recommend using the latest container agent version. For information about checking your agent version and updating to the latest version, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-update.html">Updating the Amazon ECS Container Agent</a> in the <i>Amazon Elastic Container Service Developer Guide</i>. If you're using an Amazon ECS-optimized Linux AMI, your instance needs at least version 1.26.0-1 of the <code>ecs-init</code> package. If your container instances are launched from version <code>20190301</code> or later, then they contain the required versions of the container agent and <code>ecs-init</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html">Amazon ECS-optimized Linux AMI</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>The valid values for Fargate are 2-120 seconds.</p>"""
    version_consistency: NotRequired[
        "capo_ecs.types.version_consistency.VersionConsistency"
    ]
    """<p>Specifies whether Amazon ECS will resolve the container image tag provided in the container definition to an image digest. By default, the value is <code>enabled</code>. If you set the value for a container as <code>disabled</code>, Amazon ECS will not resolve the provided container image tag to a digest and will use the original image URI specified in the container definition for deployment. For more information about container image resolution, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html#deployment-container-image-stability">Container image resolution</a> in the <i>Amazon ECS Developer Guide</i>.</p>"""
    hostname: NotRequired["capo_ecs.types.string.String"]
    """<p>The hostname to use for your container. This parameter maps to <code>Hostname</code> in the docker container create command and the <code>--hostname</code> option to docker run.</p> <note> <p>The <code>hostname</code> parameter is not supported if you're using the <code>awsvpc</code> network mode.</p> </note>"""
    user: NotRequired["capo_ecs.types.string.String"]
    """<p>The user to use inside the container. This parameter maps to <code>User</code> in the docker container create command and the <code>--user</code> option to docker run.</p> <important> <p>When running tasks using the <code>host</code> network mode, don't run containers using the root user (UID 0). We recommend using a non-root user for better security.</p> </important> <p>You can specify the <code>user</code> using the following formats. If specifying a UID or GID, you must specify it as a positive integer.</p> <ul> <li> <p> <code>user</code> </p> </li> <li> <p> <code>user:group</code> </p> </li> <li> <p> <code>uid</code> </p> </li> <li> <p> <code>uid:gid</code> </p> </li> <li> <p> <code>user:gid</code> </p> </li> <li> <p> <code>uid:group</code> </p> </li> </ul> <note> <p>This parameter is not supported for Windows containers.</p> </note>"""
    working_directory: NotRequired["capo_ecs.types.string.String"]
    """<p>The working directory to run commands inside the container in. This parameter maps to <code>WorkingDir</code> in the docker container create command and the <code>--workdir</code> option to docker run.</p>"""
    disable_networking: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>When this parameter is true, networking is off within the container. This parameter maps to <code>NetworkDisabled</code> in the docker container create command.</p> <note> <p>This parameter is not supported for Windows containers.</p> </note>"""
    privileged: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>When this parameter is true, the container is given elevated privileges on the host container instance (similar to the <code>root</code> user). This parameter maps to <code>Privileged</code> in the docker container create command and the <code>--privileged</code> option to docker run</p> <note> <p>This parameter is not supported for Windows containers or tasks run on Fargate.</p> </note>"""
    readonly_root_filesystem: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>When this parameter is true, the container is given read-only access to its root file system. This parameter maps to <code>ReadonlyRootfs</code> in the docker container create command and the <code>--read-only</code> option to docker run.</p> <note> <p>This parameter is not supported for Windows containers.</p> </note>"""
    dns_servers: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>A list of DNS servers that are presented to the container. This parameter maps to <code>Dns</code> in the docker container create command and the <code>--dns</code> option to docker run.</p> <note> <p>This parameter is not supported for Windows containers.</p> </note>"""
    dns_search_domains: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>A list of DNS search domains that are presented to the container. This parameter maps to <code>DnsSearch</code> in the docker container create command and the <code>--dns-search</code> option to docker run.</p> <note> <p>This parameter is not supported for Windows containers.</p> </note>"""
    extra_hosts: NotRequired["capo_ecs.types.host_entry_list.HostEntryList"]
    """<p>A list of hostnames and IP address mappings to append to the <code>/etc/hosts</code> file on the container. This parameter maps to <code>ExtraHosts</code> in the docker container create command and the <code>--add-host</code> option to docker run.</p> <note> <p>This parameter isn't supported for Windows containers or tasks that use the <code>awsvpc</code> network mode.</p> </note>"""
    docker_security_options: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>A list of strings to provide custom configuration for multiple security systems. This field isn't valid for containers in tasks using the Fargate launch type.</p> <p>For Linux tasks on EC2, this parameter can be used to reference custom labels for SELinux and AppArmor multi-level security systems.</p> <p>For any tasks on EC2, this parameter can be used to reference a credential spec file that configures a container for Active Directory authentication. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows-gmsa.html">Using gMSAs for Windows Containers</a> and <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/linux-gmsa.html">Using gMSAs for Linux Containers</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <p>This parameter maps to <code>SecurityOpt</code> in the docker container create command and the <code>--security-opt</code> option to docker run.</p> <note> <p>The Amazon ECS container agent running on a container instance must register with the <code>ECS_SELINUX_CAPABLE=true</code> or <code>ECS_APPARMOR_CAPABLE=true</code> environment variables before containers placed on that instance can use these security options. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html">Amazon ECS Container Agent Configuration</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </note> <p>Valid values: "no-new-privileges" | "apparmor:PROFILE" | "label:value" | "credentialspec:CredentialSpecFilePath"</p>"""
    interactive: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>When this parameter is <code>true</code>, you can deploy containerized applications that require <code>stdin</code> or a <code>tty</code> to be allocated. This parameter maps to <code>OpenStdin</code> in the docker container create command and the <code>--interactive</code> option to docker run.</p>"""
    pseudo_terminal: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>When this parameter is <code>true</code>, a TTY is allocated. This parameter maps to <code>Tty</code> in the docker container create command and the <code>--tty</code> option to docker run.</p>"""
    docker_labels: NotRequired["capo_ecs.types.docker_labels_map.DockerLabelsMap"]
    """<p>A key/value map of labels to add to the container. This parameter maps to <code>Labels</code> in the docker container create command and the <code>--label</code> option to docker run. This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: <code>sudo docker version --format '{{.Server.APIVersion}}'</code> </p>"""
    ulimits: NotRequired["capo_ecs.types.ulimit_list.UlimitList"]
    """<p>A list of <code>ulimits</code> to set in the container. If a <code>ulimit</code> value is specified in a task definition, it overrides the default values set by Docker. This parameter maps to <code>Ulimits</code> in the docker container create command and the <code>--ulimit</code> option to docker run. Valid naming values are displayed in the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Ulimit.html">Ulimit</a> data type.</p> <p>Amazon ECS tasks hosted on Fargate use the default resource limit values set by the operating system with the exception of the <code>nofile</code> resource limit parameter which Fargate overrides. The <code>nofile</code> resource limit sets a restriction on the number of open files that a container can use. The default <code>nofile</code> soft limit is <code> 65535</code> and the default hard limit is <code>65535</code>.</p> <p>This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: <code>sudo docker version --format '{{.Server.APIVersion}}'</code> </p> <note> <p>This parameter is not supported for Windows containers.</p> </note>"""
    log_configuration: NotRequired["capo_ecs.types.log_configuration.LogConfiguration"]
    """<p>The log configuration specification for the container.</p> <p>This parameter maps to <code>LogConfig</code> in the docker container create command and the <code>--log-driver</code> option to docker run. By default, containers use the same logging driver that the Docker daemon uses. However the container can use a different logging driver than the Docker daemon by specifying a log driver with this parameter in the container definition. To use a different logging driver for a container, the log system must be configured properly on the container instance (or on a different log server for remote logging options). </p> <note> <p>Amazon ECS currently supports a subset of the logging drivers available to the Docker daemon (shown in the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_LogConfiguration.html">LogConfiguration</a> data type). Additional log drivers may be available in future releases of the Amazon ECS container agent.</p> </note> <p>This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: <code>sudo docker version --format '{{.Server.APIVersion}}'</code> </p> <note> <p>The Amazon ECS container agent running on a container instance must register the logging drivers available on that instance with the <code>ECS_AVAILABLE_LOGGING_DRIVERS</code> environment variable before containers placed on that instance can use these log configuration options. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-agent-config.html">Amazon ECS Container Agent Configuration</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </note>"""
    health_check: NotRequired["capo_ecs.types.health_check.HealthCheck"]
    """<p>The container health check command and associated configuration parameters for the container. This parameter maps to <code>HealthCheck</code> in the docker container create command and the <code>HEALTHCHECK</code> parameter of docker run.</p>"""
    system_controls: NotRequired["capo_ecs.types.system_controls.SystemControls"]
    """<p>A list of namespaced kernel parameters to set in the container. This parameter maps to <code>Sysctls</code> in the docker container create command and the <code>--sysctl</code> option to docker run. For example, you can configure <code>net.ipv4.tcp_keepalive_time</code> setting to maintain longer lived connections.</p>"""
    resource_requirements: NotRequired[
        "capo_ecs.types.resource_requirements.ResourceRequirements"
    ]
    """<p>The type and amount of a resource to assign to a container. The supported resources are GPUs and Neuron devices.</p>"""
    firelens_configuration: NotRequired[
        "capo_ecs.types.firelens_configuration.FirelensConfiguration"
    ]
    """<p>The FireLens configuration for the container. This is used to specify and configure a log router for container logs. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html">Custom Log Routing</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    credential_specs: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>A list of ARNs in SSM or Amazon S3 to a credential spec (<code>CredSpec</code>) file that configures the container for Active Directory authentication. We recommend that you use this parameter instead of the <code>dockerSecurityOptions</code>. The maximum number of ARNs is 1.</p> <p>There are two formats for each ARN.</p> <dl> <dt>credentialspecdomainless:MyARN</dt> <dd> <p>You use <code>credentialspecdomainless:MyARN</code> to provide a <code>CredSpec</code> with an additional section for a secret in Secrets Manager. You provide the login credentials to the domain in the secret.</p> <p>Each task that runs on any container instance can join different domains.</p> <p>You can use this format without joining the container instance to a domain.</p> </dd> <dt>credentialspec:MyARN</dt> <dd> <p>You use <code>credentialspec:MyARN</code> to provide a <code>CredSpec</code> for a single domain.</p> <p>You must join the container instance to the domain before you start any tasks that use this task definition.</p> </dd> </dl> <p>In both formats, replace <code>MyARN</code> with the ARN in SSM or Amazon S3.</p> <p>If you provide a <code>credentialspecdomainless:MyARN</code>, the <code>credspec</code> must provide a ARN in Secrets Manager for a secret containing the username, password, and the domain to connect to. For better security, the instance isn't joined to the domain for domainless authentication. Other applications on the instance can't use the domainless credentials. You can use this parameter to run tasks on the same instance, even it the tasks need to join different domains. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows-gmsa.html">Using gMSAs for Windows Containers</a> and <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/linux-gmsa.html">Using gMSAs for Linux Containers</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerDefinition) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "image" in value:
        out["image"] = value["image"]
    if "repository_credentials" in value:
        import capo_ecs.types.repository_credentials

        out["repositoryCredentials"] = (
            capo_ecs.types.repository_credentials.serialize_aws_json_1_1(
                value["repository_credentials"]
            )
        )
    out["cpu"] = value.get("cpu", 0)
    if "memory" in value:
        out["memory"] = value["memory"]
    if "memory_reservation" in value:
        out["memoryReservation"] = value["memory_reservation"]
    if "links" in value:
        import capo_ecs.types.string_list

        out["links"] = capo_ecs.types.string_list.serialize_aws_json_1_1(value["links"])
    if "port_mappings" in value:
        import capo_ecs.types.port_mapping_list

        out["portMappings"] = capo_ecs.types.port_mapping_list.serialize_aws_json_1_1(
            value["port_mappings"]
        )
    if "essential" in value:
        out["essential"] = value["essential"]
    if "restart_policy" in value:
        import capo_ecs.types.container_restart_policy

        out["restartPolicy"] = (
            capo_ecs.types.container_restart_policy.serialize_aws_json_1_1(
                value["restart_policy"]
            )
        )
    if "entry_point" in value:
        import capo_ecs.types.string_list

        out["entryPoint"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["entry_point"]
        )
    if "command" in value:
        import capo_ecs.types.string_list

        out["command"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["command"]
        )
    if "environment" in value:
        import capo_ecs.types.environment_variables

        out["environment"] = (
            capo_ecs.types.environment_variables.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "environment_files" in value:
        import capo_ecs.types.environment_files

        out["environmentFiles"] = (
            capo_ecs.types.environment_files.serialize_aws_json_1_1(
                value["environment_files"]
            )
        )
    if "mount_points" in value:
        import capo_ecs.types.mount_point_list

        out["mountPoints"] = capo_ecs.types.mount_point_list.serialize_aws_json_1_1(
            value["mount_points"]
        )
    if "volumes_from" in value:
        import capo_ecs.types.volume_from_list

        out["volumesFrom"] = capo_ecs.types.volume_from_list.serialize_aws_json_1_1(
            value["volumes_from"]
        )
    if "linux_parameters" in value:
        import capo_ecs.types.linux_parameters

        out["linuxParameters"] = capo_ecs.types.linux_parameters.serialize_aws_json_1_1(
            value["linux_parameters"]
        )
    if "secrets" in value:
        import capo_ecs.types.secret_list

        out["secrets"] = capo_ecs.types.secret_list.serialize_aws_json_1_1(
            value["secrets"]
        )
    if "depends_on" in value:
        import capo_ecs.types.container_dependencies

        out["dependsOn"] = capo_ecs.types.container_dependencies.serialize_aws_json_1_1(
            value["depends_on"]
        )
    if "start_timeout" in value:
        out["startTimeout"] = value["start_timeout"]
    if "stop_timeout" in value:
        out["stopTimeout"] = value["stop_timeout"]
    if "version_consistency" in value:
        import capo_ecs.types.version_consistency

        out["versionConsistency"] = (
            capo_ecs.types.version_consistency.serialize_aws_json_1_1(
                value["version_consistency"]
            )
        )
    if "hostname" in value:
        out["hostname"] = value["hostname"]
    if "user" in value:
        out["user"] = value["user"]
    if "working_directory" in value:
        out["workingDirectory"] = value["working_directory"]
    if "disable_networking" in value:
        out["disableNetworking"] = value["disable_networking"]
    if "privileged" in value:
        out["privileged"] = value["privileged"]
    if "readonly_root_filesystem" in value:
        out["readonlyRootFilesystem"] = value["readonly_root_filesystem"]
    if "dns_servers" in value:
        import capo_ecs.types.string_list

        out["dnsServers"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["dns_servers"]
        )
    if "dns_search_domains" in value:
        import capo_ecs.types.string_list

        out["dnsSearchDomains"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["dns_search_domains"]
        )
    if "extra_hosts" in value:
        import capo_ecs.types.host_entry_list

        out["extraHosts"] = capo_ecs.types.host_entry_list.serialize_aws_json_1_1(
            value["extra_hosts"]
        )
    if "docker_security_options" in value:
        import capo_ecs.types.string_list

        out["dockerSecurityOptions"] = (
            capo_ecs.types.string_list.serialize_aws_json_1_1(
                value["docker_security_options"]
            )
        )
    if "interactive" in value:
        out["interactive"] = value["interactive"]
    if "pseudo_terminal" in value:
        out["pseudoTerminal"] = value["pseudo_terminal"]
    if "docker_labels" in value:
        import capo_ecs.types.docker_labels_map

        out["dockerLabels"] = capo_ecs.types.docker_labels_map.serialize_aws_json_1_1(
            value["docker_labels"]
        )
    if "ulimits" in value:
        import capo_ecs.types.ulimit_list

        out["ulimits"] = capo_ecs.types.ulimit_list.serialize_aws_json_1_1(
            value["ulimits"]
        )
    if "log_configuration" in value:
        import capo_ecs.types.log_configuration

        out["logConfiguration"] = (
            capo_ecs.types.log_configuration.serialize_aws_json_1_1(
                value["log_configuration"]
            )
        )
    if "health_check" in value:
        import capo_ecs.types.health_check

        out["healthCheck"] = capo_ecs.types.health_check.serialize_aws_json_1_1(
            value["health_check"]
        )
    if "system_controls" in value:
        import capo_ecs.types.system_controls

        out["systemControls"] = capo_ecs.types.system_controls.serialize_aws_json_1_1(
            value["system_controls"]
        )
    if "resource_requirements" in value:
        import capo_ecs.types.resource_requirements

        out["resourceRequirements"] = (
            capo_ecs.types.resource_requirements.serialize_aws_json_1_1(
                value["resource_requirements"]
            )
        )
    if "firelens_configuration" in value:
        import capo_ecs.types.firelens_configuration

        out["firelensConfiguration"] = (
            capo_ecs.types.firelens_configuration.serialize_aws_json_1_1(
                value["firelens_configuration"]
            )
        )
    if "credential_specs" in value:
        import capo_ecs.types.string_list

        out["credentialSpecs"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["credential_specs"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerDefinition:
    out: ContainerDefinition = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("image") is not None:
        out["image"] = data["image"]
    if data.get("repositoryCredentials") is not None:
        import capo_ecs.types.repository_credentials

        out["repository_credentials"] = (
            capo_ecs.types.repository_credentials.deserialize_aws_json_1_1(
                data["repositoryCredentials"]
            )
        )
    if data.get("cpu") is not None:
        out["cpu"] = data["cpu"]
    else:
        out["cpu"] = 0
    if data.get("memory") is not None:
        out["memory"] = data["memory"]
    if data.get("memoryReservation") is not None:
        out["memory_reservation"] = data["memoryReservation"]
    if data.get("links") is not None:
        import capo_ecs.types.string_list

        out["links"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["links"]
        )
    if data.get("portMappings") is not None:
        import capo_ecs.types.port_mapping_list

        out["port_mappings"] = (
            capo_ecs.types.port_mapping_list.deserialize_aws_json_1_1(
                data["portMappings"]
            )
        )
    if data.get("essential") is not None:
        out["essential"] = data["essential"]
    if data.get("restartPolicy") is not None:
        import capo_ecs.types.container_restart_policy

        out["restart_policy"] = (
            capo_ecs.types.container_restart_policy.deserialize_aws_json_1_1(
                data["restartPolicy"]
            )
        )
    if data.get("entryPoint") is not None:
        import capo_ecs.types.string_list

        out["entry_point"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["entryPoint"]
        )
    if data.get("command") is not None:
        import capo_ecs.types.string_list

        out["command"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["command"]
        )
    if data.get("environment") is not None:
        import capo_ecs.types.environment_variables

        out["environment"] = (
            capo_ecs.types.environment_variables.deserialize_aws_json_1_1(
                data["environment"]
            )
        )
    if data.get("environmentFiles") is not None:
        import capo_ecs.types.environment_files

        out["environment_files"] = (
            capo_ecs.types.environment_files.deserialize_aws_json_1_1(
                data["environmentFiles"]
            )
        )
    if data.get("mountPoints") is not None:
        import capo_ecs.types.mount_point_list

        out["mount_points"] = capo_ecs.types.mount_point_list.deserialize_aws_json_1_1(
            data["mountPoints"]
        )
    if data.get("volumesFrom") is not None:
        import capo_ecs.types.volume_from_list

        out["volumes_from"] = capo_ecs.types.volume_from_list.deserialize_aws_json_1_1(
            data["volumesFrom"]
        )
    if data.get("linuxParameters") is not None:
        import capo_ecs.types.linux_parameters

        out["linux_parameters"] = (
            capo_ecs.types.linux_parameters.deserialize_aws_json_1_1(
                data["linuxParameters"]
            )
        )
    if data.get("secrets") is not None:
        import capo_ecs.types.secret_list

        out["secrets"] = capo_ecs.types.secret_list.deserialize_aws_json_1_1(
            data["secrets"]
        )
    if data.get("dependsOn") is not None:
        import capo_ecs.types.container_dependencies

        out["depends_on"] = (
            capo_ecs.types.container_dependencies.deserialize_aws_json_1_1(
                data["dependsOn"]
            )
        )
    if data.get("startTimeout") is not None:
        out["start_timeout"] = data["startTimeout"]
    if data.get("stopTimeout") is not None:
        out["stop_timeout"] = data["stopTimeout"]
    if data.get("versionConsistency") is not None:
        import capo_ecs.types.version_consistency

        out["version_consistency"] = (
            capo_ecs.types.version_consistency.deserialize_aws_json_1_1(
                data["versionConsistency"]
            )
        )
    if data.get("hostname") is not None:
        out["hostname"] = data["hostname"]
    if data.get("user") is not None:
        out["user"] = data["user"]
    if data.get("workingDirectory") is not None:
        out["working_directory"] = data["workingDirectory"]
    if data.get("disableNetworking") is not None:
        out["disable_networking"] = data["disableNetworking"]
    if data.get("privileged") is not None:
        out["privileged"] = data["privileged"]
    if data.get("readonlyRootFilesystem") is not None:
        out["readonly_root_filesystem"] = data["readonlyRootFilesystem"]
    if data.get("dnsServers") is not None:
        import capo_ecs.types.string_list

        out["dns_servers"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["dnsServers"]
        )
    if data.get("dnsSearchDomains") is not None:
        import capo_ecs.types.string_list

        out["dns_search_domains"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["dnsSearchDomains"]
        )
    if data.get("extraHosts") is not None:
        import capo_ecs.types.host_entry_list

        out["extra_hosts"] = capo_ecs.types.host_entry_list.deserialize_aws_json_1_1(
            data["extraHosts"]
        )
    if data.get("dockerSecurityOptions") is not None:
        import capo_ecs.types.string_list

        out["docker_security_options"] = (
            capo_ecs.types.string_list.deserialize_aws_json_1_1(
                data["dockerSecurityOptions"]
            )
        )
    if data.get("interactive") is not None:
        out["interactive"] = data["interactive"]
    if data.get("pseudoTerminal") is not None:
        out["pseudo_terminal"] = data["pseudoTerminal"]
    if data.get("dockerLabels") is not None:
        import capo_ecs.types.docker_labels_map

        out["docker_labels"] = (
            capo_ecs.types.docker_labels_map.deserialize_aws_json_1_1(
                data["dockerLabels"]
            )
        )
    if data.get("ulimits") is not None:
        import capo_ecs.types.ulimit_list

        out["ulimits"] = capo_ecs.types.ulimit_list.deserialize_aws_json_1_1(
            data["ulimits"]
        )
    if data.get("logConfiguration") is not None:
        import capo_ecs.types.log_configuration

        out["log_configuration"] = (
            capo_ecs.types.log_configuration.deserialize_aws_json_1_1(
                data["logConfiguration"]
            )
        )
    if data.get("healthCheck") is not None:
        import capo_ecs.types.health_check

        out["health_check"] = capo_ecs.types.health_check.deserialize_aws_json_1_1(
            data["healthCheck"]
        )
    if data.get("systemControls") is not None:
        import capo_ecs.types.system_controls

        out["system_controls"] = (
            capo_ecs.types.system_controls.deserialize_aws_json_1_1(
                data["systemControls"]
            )
        )
    if data.get("resourceRequirements") is not None:
        import capo_ecs.types.resource_requirements

        out["resource_requirements"] = (
            capo_ecs.types.resource_requirements.deserialize_aws_json_1_1(
                data["resourceRequirements"]
            )
        )
    if data.get("firelensConfiguration") is not None:
        import capo_ecs.types.firelens_configuration

        out["firelens_configuration"] = (
            capo_ecs.types.firelens_configuration.deserialize_aws_json_1_1(
                data["firelensConfiguration"]
            )
        )
    if data.get("credentialSpecs") is not None:
        import capo_ecs.types.string_list

        out["credential_specs"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["credentialSpecs"]
        )
    return out
