import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import org.json.simple.JSONObject;
import org.json.simple.JSONArray;
//import org.json.JSONTokener;
//import org.json.JSONException;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.time.LocalDate;


public class Plane {

	private static boolean isValidWord(String str) {
		if(str!=null) {
			char[] charArr = str.toCharArray();
			for(int i=0;i<charArr.length;i++) {
				if((charArr[i]<'a' || charArr[i]>'z') && (charArr[i]<'A' || charArr[i]>'Z') && charArr[i] != ' ') {
					return false;
				}
			}
			return true;
		} else {
			return false;
		}
	
	}

	private static boolean isValidRecognized(String str) {
		if(str !=null &&(str.equals("true") || str.equals("false"))) {
			return true;
		}
		return false;
	}

	private static boolean isValidCountryCode(String str){
		
		if(str!=null && str.length()==2) {
			char[] charArr = str.toCharArray();
			for(int i=0;i<charArr.length;i++) {
				if(!Character.isUpperCase(charArr[i])) {
					return false;
				}
			}
			return true;
		} else {
			return false;
		}
	}
	
	private static boolean isValidKeyId(String str) {
		if(str!=null && str.length()==16){
			return true;
		}
		return false;
	}
	
	private static boolean isValidDrawing(JSONArray arr) {
		if(arr!=null && arr.size()>=1) {
			for(int i=0;i<arr.size();i++) {
				JSONArray arr1 = (JSONArray)arr.get(i);
				if(arr1.size()!=2){
					return false;
				}
			}
			return true;
		} else {
			return false;
		}
		
	}


  public static class PlaneMapper
       extends Mapper<Object, Text, Text, IntWritable>{

    private final static IntWritable one = new IntWritable(1);
    //private Text word = new Text();
    
    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
		
		Configuration conf = context.getConfiguration();
		//JSONTokener jsonTokener = new JSONTokener(value.toString());
		JSONParser jsonParser = new JSONParser();
		try{	
			JSONObject jsonObject = (JSONObject) jsonParser.parse(value.toString());
			String aircraftName = conf.get("aircraftName");
			//aircraftName = aircraftName.toLowerCase();
			//String aircraftName = new String("airplane");			

			String aircraft = (String)jsonObject.get("word");		
			//aircraft = aircraft.toLowerCase();
			String dateTime = (String)jsonObject.get("timestamp");
			String dateOnly = dateTime.split(" ")[0];
			String[] dateArr = dateOnly.split("-");
			int yyyy = Integer.parseInt(dateArr[0]);
			int mm = Integer.parseInt(dateArr[1]);
			int dd = Integer.parseInt(dateArr[2]);
			

			if(aircraftName != null && aircraftName.equals(aircraft)) {
				String recognized = ((Boolean)jsonObject.get("recognized")).toString();
				
				LocalDate date = LocalDate.of(yyyy,mm,dd);
				int dateInt = date.getDayOfWeek().getValue();
				
				boolean isvalidWord = isValidWord(aircraft);
				boolean isvalidRecognized = isValidRecognized(recognized);
				boolean isvalidCode = isValidCountryCode((String)jsonObject.get("countrycode"));
				boolean isvalidKey = isValidKeyId((String)jsonObject.get("key_id"));
				boolean isvalidDrawing = isValidDrawing((JSONArray)jsonObject.get("drawing"));

				if(isvalidWord && isvalidRecognized && isvalidCode && isvalidKey && isvalidDrawing){
					if(recognized.equals("true")) {
						context.write(new Text(aircraft),one);
					} else if((dateInt==6 || dateInt==7) && recognized.equals("false")) {
						context.write(new Text(aircraft+'n'),one);
					}
				}
				
							
			}			

		}catch(ParseException e) {
			e.printStackTrace();
		}
    }
  }
  
  public static class PlaneCombiner
       extends Reducer<Text,IntWritable,Text,IntWritable> {
    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values,
                       Context context
                       ) throws IOException, InterruptedException {
      int sum = 0;
      for (IntWritable val : values) {
        sum += val.get();
      }
      result.set(sum);
      context.write(key, result);
    }
  }

  public static class PlaneReducer
       extends Reducer<Text,IntWritable,NullWritable,IntWritable> {
    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values,
                       Context context
                       ) throws IOException, InterruptedException {
      int sum = 0;
      for (IntWritable val : values) {
        sum += val.get();
      }
      result.set(sum);
      context.write(NullWritable.get(), result);
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    conf.set("aircraftName",args[2]);
    Job job = Job.getInstance(conf, "plane");
    job.setJarByClass(Plane.class);
    job.setMapperClass(PlaneMapper.class);
    job.setCombinerClass(PlaneCombiner.class);
    job.setReducerClass(PlaneReducer.class);
    
    job.setMapOutputKeyClass(Text.class);
	job.setMapOutputValueClass(IntWritable.class);
	
    //job.setOutputKeyClass(Text.class);
    job.setOutputKeyClass(NullWritable.class);
    job.setOutputValueClass(IntWritable.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    
    

    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
