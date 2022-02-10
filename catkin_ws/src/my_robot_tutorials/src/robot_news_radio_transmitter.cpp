#include <ros/ros.h>
#include <std_msgs/String.h>

int main(int argc, char **argv){
    //node withhout anonymous
    // ros::init(argc, argv, "robot_news_radio_transmitter");
    
    //node name with anonymous, same as python anonymous
    ros::init(argc, argv, "robot_news_radio_transmitter", ros::init_options::AnonymousName);
    ros::NodeHandle nh;

    ros::Publisher pub = nh.advertise<std_msgs::String>("/robot_news_radio", 10);

    ros::Rate rate(3);

    while(ros::ok()){
        std_msgs::String msg;
        msg.data = "Hi, this is Kevin from radio station";
        pub.publish(msg);
        rate.sleep();
    }
}