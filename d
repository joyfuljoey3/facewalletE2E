module sensor_fusion_worker {
    source = "../modules/nas-worker-service"
    namespace = "avikus-nas-core"
    app_name = "sensor-fusion-worker"
    image_pull_secrets = "docker-cfg"
    containers = [
        {
            name="sensor-fusion-worker"
            image_url="479435310497.dkr.ecr.ap-northeast-2.amazonaws.com/standard-nas-sensor-fusion"
            image_tag="v1.0.5"
            command=["sh", "-c", "/wait && ./build/NAS_sensorfusion/NAS_sensorfusion /opt/sensor-fusion"]
            image_pull_policy="IfNotPresent"
            envs = [
                {
                    "name": "DEF_CAMERA_HEIGHT_EO",
                    "value": "22.0"
                },
                {
                    "name": "DEF_CAMERA_HEIGHT_IR",
                    "value": "22.0"
                },
                {
                    "name": "DEF_TCPA_YELLOW",
                    "value": "3000.0"
                },
                {
                    "name": "DEF_DCPA_YELLOW",
                    "value": "5000.0"
                },
                {
                    "name": "DEF_TCPA_RED",
                    "value": "1500.0"
                },
                {
                    "name": "DEF_DCPA_RED",
                    "value": "2500.0"
                },
                {
                    "name": "DEF_SHIP_LENGTH",
                    "value": "299.0"
                },
                {
                    "name": "DEF_POSITION_WEIGHT",
                    "value": "1.0"
                },
                {
                    "name": "DEF_DIRECTION_WEIGHT",
                    "value": "0.0"
                },
                {
                    "name": "DEF_SIZE_WEIGHT",
                    "value": "0.0"
                },
                {
                    "name": "DEF_TIME_WEIGHT",
                    "value": "0.0"
                },
                {
                    "name": "DEF_EO_WIDTH",
                    "value": "3840"
                },
                {
                    "name": "DEF_EO_HEIGHT",
                    "value": "1080"
                },
                {
                    "name": "DEF_IR_WIDTH",
                    "value": "1536"
                },
                {
                    "name": "DEF_IR_HEIGHT",
                    "value": "512"
                },
                {
                    "name": "DEF_PANORAMA_MODE",
                    "value": "1"
                },
                {
                    "name": "DEF_CAM_FX_EO",
                    "value": "1333.3,1333.0,1339.7"
                },
                {
                    "name": "DEF_CAM_FY_EO",
                    "value": "1341.6,1340.1,1348.4"
                },
                {
                    "name": "DEF_CAM_CX_EO",
                    "value": "1012.6,1016.4,1012.1"
                },
                {
                    "name": "DEF_CAM_CY_EO",
                    "value": "676.2875,680.2051,660.1434"
                },
                {
                    "name": "DEF_CAM_ROT_LEFT_EO",
                    "value": "0.42261826,0.0,-0.90630779,0.90630779,0.0,0.42261826,0.0,-1.0,0.0"
                },
                {
                    "name": "DEF_CAM_ROT_CENTER_EO",
                    "value": "0.99996192,-0.00872654,0.0,0.0,0.0,1.0,-0.00872654,-0.99996192,0.0"
                },
                {
                    "name": "DEF_CAM_ROT_RIGHT_EO",
                    "value": "0.42261826,0.0,0.90630779,-0.90630779,0.0,0.42261826,0.0,-1.0,0.0"
                },
                {
                    "name": "DEF_ARP_Y_BIAS_EO",
                    "value": "0,0,0"
                },
                {
                    "name": "DEF_ARP_X_BIAS_CENTER_EO",
                    "value": "525"
                },
                {
                    "name": "DEF_ARP_X_BIAS_EO",
                    "value": "-750,-10,735"
                },
                {
                    "name": "DEF_PROJECTION_OFFSET_EO",
                    "value": "80"
                },
                {
                    "name": "DEF_PANO_FOV_EO",
                    "value": "180.0"
                },
                {
                    "name": "DEF_DIST_AIS_TO_CAM_EO",
                    "value": "130.0"
                },
                {
                    "name": "DEF_CAM_FX_IR",
                    "value": "1333.3,1333.0,1339.7"
                },
                {
                    "name": "DEF_CAM_FY_IR",
                    "value": "1341.6,1340.1,1348.4"
                },
                {
                    "name": "DEF_CAM_CX_IR",
                    "value": "1012.6,1016.4,1012.1"
                },
                {
                    "name": "DEF_CAM_CY_IR",
                    "value": "676.2875,680.2051,660.1434"
                },
                {
                    "name": "DEF_CAM_ROT_LEFT_IR",
                    "value": "0.42261826,0.0,-0.90630779,0.90630779,0.0,0.42261826,0.0,-1.0,0.0"
                },
                {
                    "name": "DEF_CAM_ROT_CENTER_IR",
                    "value": "0.99996192,-0.00872654,0.0,0.0,0.0,1.0,-0.00872654,-0.99996192,0.0"
                },
                {
                    "name": "DEF_CAM_ROT_RIGHT_IR",
                    "value": "0.42261826,0.0,0.90630779,-0.90630779,0.0,0.42261826,0.0,-1.0,0.0"
                },
                {
                    "name": "DEF_ARP_Y_BIAS_IR",
                    "value": "0,0,0"
                },
                {
                    "name": "DEF_ARP_X_BIAS_CENTER_IR",
                    "value": "525"
                },
                {
                    "name": "DEF_ARP_X_BIAS_IR",
                    "value": "-750,-10,735"
                },
                {
                    "name": "DEF_SF_LOGGER_ON",
                    "value": "0"
                },
                {
                    "name": "DEF_REMOVE_LOGFILE",
                    "value": "1"
                },
                {
                    "name": "VDR_REDIS_IP",
                    "value": "redis.avikus-database"
                },
                {
                    "name": "VDR_REDIS_PORT",
                    "value": "6379"
                },
                {
                    "name": "NAS_REDIS_IP",
                    "value": "redis.avikus-database"
                },
                {
                    "name": "NAS_REDIS_PORT",
                    "value": "6379"
                },
                {
                    "name": "DEF_PROCESS_TIME",
                    "value": "100"
                },
                {
                    "name": "DEF_DATAIO_TIME",
                    "value": "200"
                },
                {
                    "name": "DEF_LOGGING_TIME",
                    "value": "5000"
                },
                {
                    "name": "DEF_FILE_SIZE",
                    "value": "147456"
                },
                {
                    "name": "DEF_NUM_OF_FILE",
                    "value": "144"
                },
                {
                    "name": "DEF_EXPIRE_TIME",
                    "value": "2"
                },
                {
                    "name": "DEF_NUM_OF_WEB_TARGET",
                    "value": "40"
                },
                {
                    "name": "DEF_NUM_OF_WEB_TARGET_RADAR",
                    "value": "3"
                },
                {
                    "name": "DEF_INF_SORT_PRIOR_THRESHOLD",
                    "value": "0.4375"
                },
                {
                    "name": "DEF_INF_THRESHOLD_EO",
                    "value": "0.375"
                },
                {
                    "name": "DEF_INF_THRESHOLD_IR",
                    "value": "0.375"
                },
                {
                    "name": "DEF_INF_THRESHOLD_FAR",
                    "value": "0.4375"
                },
                {
                    "name": "DEF_ALLOW_TRK_RADAR_ONLY",
                    "value": "1"
                },
                {
                    "name": "DEF_ALLOW_TRK_CAMERA_ONLY",
                    "value": "1"
                },
                {
                    "name": "DEF_TTM_TRUE_RELATIVE_BEARING",
                    "value": "0"
                },
                {
                    "name": "DEF_TTM_TRUE_RELATIVE_COG",
                    "value": "0"
                },
                {
                    "name": "DEF_RULE_OVERLAPPED_BOX",
                    "value": "3"
                },
                {
                    "name": "DEF_USE_EO_DETECTION",
                    "value": "1"
                },
                {
                    "name": "DEF_USE_IR_DETECTION",
                    "value": "1"
                },
                {
                    "name": "DEF_FAST_PLAY",
                    "value": "0"
                },
                {
                    "name": "DEF_VIRTUAL_ON",
                    "value": "0"
                },
                {
                    "name": "DEF_VIRTUAL_MODE",
                    "value": "0"
                },
                {
                    "name": "OPENSEA_MIN_WARNING_CPA",
                    "value": "2"
                },
                {
                    "name": "OPENSEA_MAX_WARNING_CPA",
                    "value": "4"
                },
                {
                    "name": "OPENSEA_MIN_WARNING_TCPA",
                    "value": "10"
                },
                {
                    "name": "OPENSEA_MAX_WARNING_TCPA",
                    "value": "15"
                },
                {
                    "name": "OPENSEA_MIN_WARNING_DIST",
                    "value": "2"
                },
                {
                    "name": "OPENSEA_MAX_WARNING_DIST",
                    "value": "4"
                },
                {
                    "name": "CONGESTED_MIN_WARNING_CPA",
                    "value": "1"
                },
                {
                    "name": "CONGESTED_MAX_WARNING_CPA",
                    "value": "2"
                },
                {
                    "name": "CONGESTED_MIN_WARNING_TCPA",
                    "value": "5"
                },
                {
                    "name": "CONGESTED_MAX_WARNING_TCPA",
                    "value": "10"
                },
                {
                    "name": "CONGESTED_MIN_WARNING_DIST",
                    "value": "1"
                },
                {
                    "name": "CONGESTED_MAX_WARNING_DIST",
                    "value": "2"
                },
                {
                    "name": "WAIT_HOSTS",
                    "value": "redis.avikus-database:6379"
                }
            ]
        }
    ]
}
