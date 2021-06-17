<template>
<!--  <div style="position: relative;top: 150px;">-->
  <div id="main">
    <el-upload
        ref="upload"
        class="upload-demo"
        action="api/upload/"
        :name="'file'"
        :on-preview="handlePreview"
        accept=".csv"
        :on-remove="handleRemove"
        :multiple="false"
        :limit="1"
        :on-exceed="handleExceed"
        :before-upload="beforeUpload"
        :on-success="uploadSuccess"
        :on-error="uploadError"
        :show-file-list="false"
        :file-list="fileList"
    >
      <press-button :label="'上传文件'"
                    v-loading.fullscreen.lock="fullscreenLoading"></press-button>

      <template #tip>
        <div class="el-upload__tip upload-tip" style="display: inline;">只能上传 csv 文件，且不超过 1MB</div>
      </template>
    </el-upload>
<!--    <el-tooltip class="item" effect="dark" content="点击下载示例数据" placement="left-start">-->
<!--      <a href="example.csv" download="example.csv">-->
<!--        <el-button icon="el-icon-s-marketing" circle class="download-button" type="primary"></el-button>-->
<!--      </a>-->
<!--    </el-tooltip>-->
    <el-dialog title="选择要分析的列"
               :visible="showSelectDialog"
               @close="showSelectDialog = false"
               width="250px"
               center>
      <el-select v-model="selectColumn" placeholder="请选择">
        <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
        </el-option>
      </el-select>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="showSelectDialog = false">取 消</el-button>
          <el-button type="primary" @click="confirmSelect" >确 定</el-button>
        </span>
      </template>
    </el-dialog>

    <el-dialog :visible="showResultDialog"
               @close="showResultDialog = false"
               width="660px"
               center>
      <el-image :src="imgUrl">
        <template #placeholder>
          <div class="image-slot">
            加载中<span class="dot">...</span>
          </div>
        </template>
      </el-image>
    </el-dialog>
      <el-row  style="opacity: .8">
        <el-col :span="8">
          <el-card shadow="hover">
            <div slot="header" class="card-head-title">
              <i><img src="~@/assets/about.png" alt=""></i>
              <span>关于</span>
            </div>
            <div>
              <p class="context">
                <b>ARIMA模型:</b><br>
                对时间序列数据进行分析和预测比较完善和精确的算法是博克思-詹金斯(Box-Jenkins)方法，其常用模型包括：......
              </p>
              <el-link type="primary" style="top: 30px;"><el-button @click="aboutVisible = true" icon="el-icon-right">详细信息</el-button></el-link>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card shadow="hover">
            <div slot="header" class="card-head-title">
              <i><img src="~@/assets/data.png" alt=""></i>
              <span>数据集</span>
            </div>
            <div>
              <p class="context content">
                <b>数据格式: </b>
                <br>
                上传的数据格式应为csv格式文件，第一列为时间索引，以及至少拥有一列具有回归特效的数据。
                <el-tooltip class="item" effect="dark" content="点击下载示例数据" placement="left-start">
                  <el-link href="example.csv" download="example.csv"
                           style="top: 64px"><el-button icon="el-icon-download">下载样例</el-button></el-link>
                </el-tooltip>
              </p>
            </div>
          </el-card>
        </el-col>
        <el-col :span="8">
          <el-card shadow="hover">
            <div slot="header" class="card-head-title">
              <i><img src="~@/assets/contact.png" alt=""></i>
              <span>联系我们</span>
            </div>
            <div>
              <p class="context content">
                如果你对该项目有疑问，欢迎与我们联系：
                <br>导师：朝鲁蒙
                <el-tooltip class="item" effect="dark" content="点击复制微信号" placement="right-start">
                  <img src="img/wechat.png" style="height: 25px;position: relative;top: 5px;left: 5px;" @click="copy('clmjet')"/>
                </el-tooltip>
                <br>作者：杨佩锦
                <el-tooltip class="item" effect="dark" content="点击复制微信号" placement="right-start">
                  <img src="img/wechat.png" style="height: 25px;position: relative;top: 5px;left: 5px;" @click="copy('ypj-java')"/>
                </el-tooltip>
                <br>作者邮箱: ypj-java@qq.com
                <el-link href="mailto:ypj-java@qq.com" style="top: 30px;"><el-button icon="el-icon-message">发送邮件</el-button></el-link>
              </p>
            </div>
          </el-card>
        </el-col>
      </el-row>
      <el-dialog :visible.sync="aboutVisible" width="700px">
        <h2 slot="title">
          About<i class="el-icon-info"></i>
        </h2>
        <div style="font-size: 20px;text-align: left;line-height: 30px">
          <p><b>原理:</b> </p>
          <p>对时间序列数据进行分析和预测比较完善和精确的算法是博克思-詹金斯(Box-Jenkins)方法，其常用模型包括：自回归模型（AR模型）、
            滑动平均模型（MA模型）、（自回归-滑动平均混合模型）ARMA模型、（差分整合移动平均自回归模型）ARIMA模型。</p>
          <p>ARIMA模型（英语：Autoregressive Integrated Moving Average model），差分整合移动平均自回归模型，
            又称整合移动平均自回归模型（移动也可称作滑动），是时间序列预测分析方法之一。ARIMA(p，d，q)中，AR是“自回归”，
            p为自回归项数；MA为“滑动平均”，q为滑动平均项数，d为使之成为平稳序列所做的差分次数（阶数）。</p>
          <p>本系统会对不同的q、d、q值进行分析，选取其中最好的参数，给出预测结果</p>
          <p><b>结果:</b></p>
          <p>分析成功会，会展示一张折线图，蓝色的线条为初始数据，红色的为预测数据</p>
          <p><el-link type="primary">http://vue.ypjava.top/timesequence/</el-link>.</p>
        </div>
      </el-dialog>

    </div>
<!--  </div>-->
</template>

<script>
import PressButton from "./ui/pressButton";
import axios from "axios";
export default {
  name: "mainPage",
  components: {PressButton},
  data() {
    return {
      fileList: [],
      fullscreenLoading: false,
      showSelectDialog: false,
      showResultDialog: false,
      aboutVisible: false,
      options: [{
        label: '',
        value: 0
      }],
      title: '',
      fileName: '',
      selectColumn: 0,
      imgUrl: ''
    };
  },
  methods: {
    handleRemove(file, fileList) {
      window.console.log(file, fileList);
    },
    handlePreview(file) {
      window.console.log(file);
    },
    handleExceed(files, fileList) {
      this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
    },
    beforeUpload(file) {
      if(file.size > 1024*1024) {
        this.$notify({
          title: '错误',
          message: file.name + '文件不能大于1M，请重新上传',
          type: 'error'
        });
        return false;
      }
      // this.showSelectDialog = true;
      this.fullscreenLoading = true;
      window.console.log("上传前");
    },
    uploadSuccess(response, file) {
      this.$refs.upload.clearFiles();
      this.showSelectDialog = true;
      this.fullscreenLoading = false;
      if(response['code'] !== 200) {
        this.$notify({
          title: '错误',
          message: response['msg'],
          type: 'error'
        });
      }else {
        this.$notify({
          title: '成功',
          message: '上传 '+ file.name +' 成功',
          type: 'success'
        });
        this.options = response['data']['columns'];
        this.title = response['data']['title'];
        this.fileName = response['data']['fileName']
      }

      window.console.log("上传成功");
    },
    uploadError() {
      this.fullscreenLoading = false;
      this.$notify.error({
        title: '错误',
        message: '上传错误'
      });
      window.console.log("上传失败");
    },
    confirmSelect() {
      this.showSelectDialog = false;

      const loading = this.$loading({
        lock: true,
        text: '正在分析中',
        spinner: 'el-icon-loading',
        background: 'rgba(0, 0, 0, 0.7)'
      });

      axios.get('api/sequence/', {
        params: {
          fileName: this.fileName,
          title: this.title,
          column: this.selectColumn
        }
      }).then((response)=>{
        response = response.data;
        if(response["code"] !== 200) {
          this.$notify({
            title: '错误',
            message: response['msg'],
            type: 'error'
          });
        }else {
          this.$notify({
            title: '成功',
            message: '分析成功',
            type: 'success'
          });
          this.imgUrl = "api/static/"+response['data'];
          this.showResultDialog = true;
        }
      }).catch(error=>{
        window.console.log(error);
      }).finally(()=>{
        loading.close();
      })
    },
    copy(data) {
      let url = data
      let oInput = document.createElement('input')
      oInput.value = url
      document.body.appendChild(oInput)
      oInput.select() // 选择对象
      document.execCommand("Copy") // 执行浏览器复制命令
      this.$message({
        message: '微信号已复制到您的粘贴板',
        type: 'success'
      })
      oInput.remove()
    },
  }
}
</script>

<style scoped>
.upload-tip {
  position: relative;
  top: 10px;
  font-size: 20px;
  font-weight: initial;
  background-color: aliceblue;
  width: 330px;
  /*margin: 10px auto 30px;*/
  display: block;
  margin: 20px;
}
.download-button {
  position: fixed;
  bottom: 100px;
  right: 80px;
  width: 60px;
  height: 60px;
  font-size: 30px;
}

#main{
  width: 900px;
  margin:0px auto 80px ;
}
i img{
  width:30px;
  height: 30px;
  position: relative;
  top:5px;
  right: 5px;
}
.el-card{
  height:380px;
  line-height: 2rem;
  margin:40px 10px 10px ;

}
.content{
  height:140px;
}
.el-card__body{
  background-color: #fff;
  padding:15px 20px;
}
.card-head-title {
  height: 50px;
}
.card-head-title img {
  /*height: 50px;*/
}
.card-head-title span {
  font-size: 20px;
  line-height: 60px !important;
}

</style>
