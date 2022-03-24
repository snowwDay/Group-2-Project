import React from 'react'
import { SafeAreaView, View, Text, Image, StyleSheet } from 'react-native'

export default function LoginScreen() {
    return (
        <SafeAreaView style={{backgroundColor: '#f56423', flex: 1}}>
            <View style={styles.logoImage}>
                <Image />
                <Text>LOGO GOES HERE</Text>
            </View>

            <View style={styles.loginForm}>
                <Text>USERNAME FIELD</Text>
                <Text>PASSWORD FIELD</Text>
            </View>
        </SafeAreaView>
    )
}

const styles = StyleSheet.create({
    logoImage:{
        backgroundColor: 'grey',
        width: '75%',
        height: '35%',
        alignItems: 'center',
        marginVertical: '15%',
        marginHorizontal: '13%',
    },
    loginForm: {
        backgroundColor: 'grey',
        width: '75%',
        height: '45%',
        alignItems: 'center',
        marginHorizontal: '13%',
    }
})