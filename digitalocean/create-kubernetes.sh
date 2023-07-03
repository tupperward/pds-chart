#!/usr/bin/env bash

set -e

while getopts c:k: args
do
    case "${args}" in
        c) context=${OPTARG};;
        k) cluster=${OPTARG};;
    esac
done

doctl --context "$context" kubernetes cluster create "$cluster"
