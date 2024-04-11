const { S3Client, ListBucketsCommand, S3 } = require("@aws-sdk/client-s3");

const client = new S3({
  region: "eu-central-003",
  endpoint: "https://s3.eu-central-003.backblazeb2.com",
  credentials: {
    accessKeyId: "003e3fd5b2ea0300000000032",
    secretAccessKey: "K0034SeyL7XSOgqNICppaec5Y488IUo",
  },
});

client
  .listBuckets()
  .then((res) => console.log(res))
  .catch((err) => console.error(err));

class b2 extends S3 {

  static getFiles(configs , callback){

  }
}
