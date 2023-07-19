DROP IF EXIST config;
DROP IF EXIST keyValues;
CREATE TABLE config (
    id VARCHAR(256) PRIMARY KEY,
    body_type VARCHAR(256) DEFAULT NULL,
    body_wrapper VARCHAR(256) DEFAULT NULL,
    category VARCHAR(256) DEFAULT NULL,
    credit_free VARCHAR(256) DEFAULT NULL,
    method VARCHAR(256) DEFAULT NULL,
    request_type VARCHAR(256) DEFAULT NULL,
    url VARCHAR(256) DEFAULT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    modified_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE keyValues (
    id VARCHAR(256) PRIMARY KEY,
    config_id VARCHAR(256),
    doc_type VARCHAR(256),
    name VARCHAR(100),
    type VARCHAR(255) DEFAULT NULL,
    value VARCHAR(255) DEFAULT NULL,
    FOREIGN KEY (config_id) REFERENCES config (id)
);