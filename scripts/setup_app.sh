#!/bin/bash

# This script sets up the application

SRC_DIR=$(cd "$(dirname "$0")"; pwd -P)

$SRC_DIR/setup_app/migrate_database.sh
