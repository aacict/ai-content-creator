#!/bin/bash
set -e

rm -rf package lambda.zip

mkdir package
pip install -r requirements.txt -t package

cp -r lambda/* package/

cd package
zip -r ../lambda.zip .
cd ..

echo "✅ Lambda package created"
